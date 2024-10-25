from jinja2 import Environment, select_autoescape, FileSystemLoader
import pandas as pd
from pathlib import Path
import subprocess
import datetime
import os
import uuid
import argparse
import sys
from enum import Enum
import git
import precice

default_precice_config_params = {
    'max_used_iterations': 10,
    'time_windows_reused': 5,
}


class Experiments(Enum):
    POLYNOMIAL0 = 'poly0'
    POLYNOMIAL1 = 'poly1'
    POLYNOMIAL2 = 'poly2'
    TRIGONOMETRIC = 'tri'


def render(template_path, precice_config_params):
    base_path = Path(__file__).parent.absolute()

    env = Environment(
        loader=FileSystemLoader(base_path),
        autoescape=select_autoescape(['xml'])
    )

    precice_config_template = env.get_template(template_path)

    precice_config_name = base_path / "precice-config.xml"

    with open(precice_config_name, "w") as file:
        file.write(precice_config_template.render(precice_config_params))


def do_run(template_path, precice_config_params, participants):
    render(template_path, precice_config_params)
    print(f"{datetime.datetime.now()}: Start run with parameters {precice_config_params}")
    print("Running...")

    for name, participant in participants.items():
        participant['logfile'] = f"stdout-{name}.log"

    for participant in participants.values():
        with open(participant['root'] / participant['logfile'], "w") as outfile:
            cmd = participant["exec"] + participant["params"] + \
                [f"{keyword}={value}" for keyword, value in participant['kwargs'].items()]
            p = subprocess.Popen(cmd,
                                 cwd=participant['root'],
                                 stdout=outfile)
            participant["proc"] = p

    for participant in participants.values():
        participant["proc"].wait()

    for participant in participants.values():
        if participant["proc"].returncode != 0:
            raise Exception(f'Experiment failed. See logs {[p["logfile"] for p in participants]}')

    print("Done.")
    print("Postprocessing...")
    time_window_size = precice_config_params['time_window_size']
    summary = {"time window size": time_window_size}
    for name, participant in participants.items():
        # store iterations
        df = pd.read_csv(participant['root'] / f"precice-{name}-iterations.log",delim_whitespace=True)
        summary[f"substeps {name}"] = participant['kwargs']['--substeps']
        summary[f"avg(iterations / window)"] = df["Iterations"].mean()
        summary[f"max(iterations / window)"] = df["Iterations"].max()
        # store errors
        df = pd.read_csv(participant['root'] / f"errors-{name}.csv", comment="#")
        summary[f"time step size {name}"] = time_window_size / participant['kwargs']['--substeps']
        summary[f"error {name}"] = df["errors"].abs().max()
    print("Done.")

    return summary


if __name__ == "__main__":
    n_supported_participants = 2

    parser = argparse.ArgumentParser(description="Solving heat equation for simple or complex interface case")
    parser.add_argument(
        "template_path",
        help="template for the preCICE configuration file",
        type=str)
    parser.add_argument(
        "-T",
        "--max-time",
        help="Max simulation time",
        type=float,
        default=1.0)
    parser.add_argument(
        "-dt",
        "--base-time-window-size",
        help="Base time window / time step size",
        type=float,
        default=0.1)
    parser.add_argument(
        "-w",
        "--time-window-refinements",
        help="Number of refinements by factor 2 for the time window size",
        type=int,
        default=5)
    parser.add_argument(
        "-sb",
        "--base-time-step-refinement",
        help="Base factor for time window size / time step size",
        type=int,
        nargs=n_supported_participants,
        default=n_supported_participants * [1])
    parser.add_argument(
        "-s",
        "--time-step-refinements",
        help="Number of refinements by factor 2 for the time step size ( >1 will result in subcycling)",
        type=int,
        default=1)
    parser.add_argument(
        "-sf",
        "--time-step-refinement-factor",
        help="Factor of time step refinements for each participant (use 1, if you want to use a fixed time step / time window relationship for one participant while refining the time steps for the other participant)",
        type=int,
        nargs=n_supported_participants,
        default=n_supported_participants *
        [2])
    # add solver specific arguments below, if needed
    parser.add_argument("-e", "--experiment", help="Provide identifier for a specific experiment",
                        choices=[e.value for e in Experiments], default=Experiments.POLYNOMIAL0.value)
    parser.add_argument(
        "-tss",
        "--time-stepping-scheme",
        help="Define time stepping scheme used by each solver",
        type=str,
        nargs=n_supported_participants,
        default=n_supported_participants * ["ImplicitEuler"])
    parser.add_argument(
        "-wd",
        "--waveform-degree",
        help="Waveform degree being used",
        type=int,
        default=1)
    parser.add_argument(
        "-es",
        "--exchange-substeps",
        help="Turn exchange of substeps on/off.",
        action="store_true")
    args = parser.parse_args()

    df = pd.DataFrame()

    precice_config_params = {
        'time_window_size': None,  # will be defined later
        'max_time': args.max_time,
        'waveform_degree': args.waveform_degree,
        'substeps': args.exchange_substeps,
    }

    root_folder = Path(__file__).parent.absolute()

    participants = {
        "Dirichlet": {
            "root": root_folder / "dirichlet-fenics",
            # how to execute the participant, e.g. python3 script.py
            "exec": [".venv/bin/python3", f"../solver-fenics/{'heat.py' if args.time_stepping_scheme[0] == 'ImplicitEuler' else 'heatHigherOrder.py'}"],
            # list of positional arguments that will be used. Results in python3 script.py param1 ...
            "params": ["Dirichlet"],
            "kwargs": {  # dict with keyword arguments that will be used. Results in python3 script.py param1 ... k1=v1 k2=v2 ...
                '--time-stepping': args.time_stepping_scheme[0],
                '--substeps': None,  # will be defined later
                '--error-tol': 10e10,
            },
        },
        "Neumann": {
            "root": root_folder / "neumann-fenics",
            "exec": [".venv/bin/python3", f"../solver-fenics/{'heat.py' if args.time_stepping_scheme[0] == 'ImplicitEuler' else 'heatHigherOrder.py'}"],
            # list of positional arguments that will be used. Results in python3 script.py param1 ...
            "params": ["Neumann"],
            "kwargs": {  # dict with keyword arguments that will be used. Results in python3 script.py param1 ... k1=v1 k2=v2 ...
                '--time-stepping': args.time_stepping_scheme[1],
                '--substeps': None,  # will be defined later
                '--error-tol': 10e10,
            },
        },
    }

    for p in participants.values():
        p["kwargs"]['-g'] = args.experiment

    summary_file = Path("convergence-studies") / f"{uuid.uuid4()}.csv"

    for dt in [args.base_time_window_size * 0.5**i for i in range(args.time_window_refinements)]:
        for refinement in range(args.time_step_refinements):
            precice_config_params['time_window_size'] = dt
            i = 0
            for p in participants.values():
                p['kwargs']['--substeps'] = args.base_time_step_refinement[i] * \
                    args.time_step_refinement_factor[i]**refinement
                i += 1

            summary = do_run(args.template_path, precice_config_params, participants)
            df = pd.concat([df, pd.DataFrame(summary, index=[0])], ignore_index=True)

            print(f"Write preliminary output to {summary_file}")
            df.to_csv(summary_file)

            term_size = os.get_terminal_size()
            print('-' * term_size.columns)
            print(df)
            print('-' * term_size.columns)

    df = df.set_index(['time window size', 'time step size Dirichlet', 'time step size Neumann'])
    print(f"Write final output to {summary_file}")

    repo = git.Repo(__file__, search_parent_directories=True)
    chash = str(repo.head.commit)[:7]
    if repo.is_dirty():
        chash += "-dirty"

    metadata = {
        "git repository": repo.remotes.origin.url,
        "git commit": chash,
        "precice.get_version_information()": precice.get_version_information(),
        "precice.__version__": precice.__version__,
        "run cmd": "python3 " + " ".join(sys.argv),
        "args": args,
        "precice_config_params": precice_config_params,
        "participants": participants,
    }

    summary_file.unlink()

    with open(summary_file, 'a') as f:
        for key, value in metadata.items():
            f.write(f"# {key}:{value}\n")
        df.to_csv(f)

    print('-' * term_size.columns)
    for key, value in metadata.items():
        print(f"{key}:{value}")
    print()
    print(df)
    print('-' * term_size.columns)
