from jinja2 import Environment, select_autoescape, FileSystemLoader
import pandas as pd
from pathlib import Path
import subprocess
import datetime
import os
import uuid
import argparse
import sys


default_precice_config_params = {
    'max_used_iterations': 10,
    'time_windows_reused': 5,
}


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
            raise Exception(f'Experiment failed. See logs {[p["logfile"] for p in participants.values()]}')

    print("Done.")
    print("Postprocessing...")
    time_window_size = precice_config_params['time_window_size']
    summary = {"time window size": time_window_size}
    for name, participant in participants.items():
        df = pd.read_csv(participant['root'] / f"precice-{name}-iterations.log",delim_whitespace=True)
        summary[f"substeps {name}"] = participant['kwargs']['--substeps']
        summary[f"avg(iterations / window)"] = df["Iterations"].mean()
        
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
        'waveform_degree': args.waveform_degree,
        'substeps': args.exchange_substeps,
    }

    root_folder = Path(__file__).parent.absolute()

    participants = {
        "Dirichlet": {
            "root": root_folder / "dirichlet-fenics",
            # how to execute the participant, e.g. python3 script.py
            "exec": [".venv/bin/python3", f"../solver-fenics/heat.py"],
            # list of positional arguments that will be used. Results in python3 script.py param1 ...
            "params": ["Dirichlet"],
            "kwargs": {  # dict with keyword arguments that will be used. Results in python3 script.py param1 ... k1=v1 k2=v2 ...
                '--substeps': None,  # will be defined later
                '--error-tol': 10e10,
                '-g': 'triAcc',
            },
        },
        "Neumann": {
            "root": root_folder / "neumann-fenics",
            "exec": [".venv/bin/python3", f"../solver-fenics/heat.py"],
            # list of positional arguments that will be used. Results in python3 script.py param1 ...
            "params": ["Neumann"],
            "kwargs": {  # dict with keyword arguments that will be used. Results in python3 script.py param1 ... k1=v1 k2=v2 ...
                '--substeps': None,  # will be defined later
                '--error-tol': 10e10,
                '-g': 'triAcc',
            },
        },
    }

    summary_file = Path("acceleration-studies") / f"{uuid.uuid4()}.csv"

    for dt in [5.0, 2.0, 1.0, 0.5, 0.2, 0.1]:
        refinements = {
            "Dirichlet" : [1,3,5],
            "Neumann" : [1,3,5],
        }
        precice_config_params['time_window_size'] = dt
        for refinement_first in refinements["Dirichlet"]:
            participants["Dirichlet"]['kwargs']['--substeps'] = refinement_first
            for refinement_second in refinements["Neumann"]:
                participants["Neumann"]['kwargs']['--substeps'] = refinement_second
                summary = do_run(args.template_path, precice_config_params, participants)
                df = pd.concat([df, pd.DataFrame(summary, index=[0])], ignore_index=True)

                print(f"Write preliminary output to {summary_file}")
                df.to_csv(summary_file)

                term_size = os.get_terminal_size()
                print('-' * term_size.columns)
                print(df)
                print('-' * term_size.columns)

    df = df.set_index(['time window size', 'substeps Dirichlet', 'substeps Neumann'])
    print(f"Write final output to {summary_file}")

    import git
    # import precice

    repo = git.Repo(__file__, search_parent_directories=True)
    chash = str(repo.head.commit)[:7]
    if repo.is_dirty():
        chash += "-dirty"

    metadata = {
        "git repository": repo.remotes.origin.url,
        "git commit": chash,
        # "precice.get_version_information()": precice.get_version_information(),
        # "precice.__version__": precice.__version__,
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

