import pandas as pd
from pathlib import Path
import uuid
import argparse
from enum import Enum

import datetime

from prepesthel.participant import Participant, Participants
from prepesthel.runner import run
from prepesthel.io import Results, Executors

default_precice_config_params = {
    'max_used_iterations': 10,
    'time_windows_reused': 5,
}


class Experiments(Enum):
    POLYNOMIAL = 'poly'
    POLYNOMIAL2 = 'poly2'
    POLYNOMIAL3 = 'poly3'
    POLYNOMIAL4 = 'poly4'
    TRIGONOMETRIC = 'tri'
    SINCOS = 'sincos'


def postproc(participants: Participants, precice_config_params=None):
    print(f"{datetime.datetime.now()}: Postprocessing...")

    time_window_size = precice_config_params['time_window_size']
    summary = {"time window size": time_window_size}
    for participant in participants.values():
        # store iterations
        df = pd.read_csv(participant.root / f"precice-{participant.name}-iterations.log",sep="\s+")
        summary[f"substeps {participant.name}"] = participant.kwargs['--substeps']
        summary[f"avg(iterations / window)"] = df["Iterations"].mean()
        summary[f"max(iterations / window)"] = df["Iterations"].max()
        # store errors
        df = pd.read_csv(participant.root / f"output-{participant.name}.csv", comment="#")
        summary[f"time step size {participant.name}"] = time_window_size / participant.kwargs['--substeps']
        summary[f"error {participant.name}"] = df["errors"].abs().max()

    print(f"{datetime.datetime.now()}: Done.")

    return summary



if __name__ == "__main__":
    n_supported_participants = 2

    parser = argparse.ArgumentParser(description="Solving heat equation for simple or complex interface case")
    parser.add_argument(
        "template_path",
        help="template for the preCICE configuration file",
        type=str)
    parser.add_argument(
        "--silent",
        help="Deactivates result output to command line",
        action='store_true')
    parser.add_argument(
        "--executor",
        help="Define type of executor",
        type=str,
        choices=[e.value for e in Executors],
        default=Executors.LOCAL.value)
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
                        choices=[e.value for e in Experiments], default=Experiments.POLYNOMIAL.value)
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
    parser.add_argument(
        "-o",
        "--out-filename",
        help="Provide a file name. If no file name is provided a UUID will be generated as name. Abort if file already exists.",
        type=str,
    )
    args = parser.parse_args()

    df = pd.DataFrame()

    precice_config_params = {
        'time_window_size': None,  # will be defined later
        'max_time': args.max_time,
        'waveform_degree': args.waveform_degree,
        'substeps': args.exchange_substeps,
    }

    root_folder = Path(__file__).parent.absolute()

    # Define how participants will be executed here
    participants: Participants = {
        "Dirichlet": Participant(
            "Dirichlet", 
            root_folder / "dirichlet-fenics",
            ["../.venv/bin/python3", f"../solver-fenics/{'heat.py' if args.time_stepping_scheme[0] == 'ImplicitEuler' else 'heatHigherOrder.py'}"], 
            ["Dirichlet"], 
            {  # dict with keyword arguments that will be used. Results in python3 script.py param1 ... k1=v1 k2=v2 ...
                '--time-stepping': args.time_stepping_scheme[0],
                '--substeps': None,  # will be defined later
                '--error-tol': 10e10,
                '-g': args.experiment,
            },
        ),
        "Neumann": Participant(
            "Neumann", 
            root_folder / "neumann-fenics",
            ["../.venv/bin/python3", f"../solver-fenics/{'heat.py' if args.time_stepping_scheme[1] == 'ImplicitEuler' else 'heatHigherOrder.py'}"],
            ["Neumann"], 
            {  # dict with keyword arguments that will be used. Results in python3 script.py param1 ... k1=v1 k2=v2 ...
                '--time-stepping': args.time_stepping_scheme[1],
                '--substeps': None,  # will be defined later
                '--error-tol': 10e10,
                '-g': args.experiment,
            },
        ),
    }

    if len(participants) != n_supported_participants:
        raise Exception(f"Currently only supports coupling of {n_supported_participants} participants")

    results_file_path = root_folder
    if args.out_filename:  # use file name given by user
        results_file_path = results_file_path / args.out_filename
    else:  # no file name is given. Create UUID for file name
        results_file_path = results_file_path / "convergence-studies" / f"{uuid.uuid4()}.csv"

    results = Results(results_file_path)

    for dt in [args.base_time_window_size * 0.5**i for i in range(args.time_window_refinements)]:
        for refinement in range(args.time_step_refinements):
            precice_config_params['time_window_size'] = dt
            i = 0
            for p in participants.values():
                p.kwargs['--substeps'] = args.base_time_step_refinement[i] * \
                    args.time_step_refinement_factor[i]**refinement
                i += 1

            run(participants, args.template_path, precice_config_params)
            summary = postproc(participants, precice_config_params)

            results.append(summary)
            results.output_preliminary(silent=args.silent)

    results.output_final(participants, args, precice_config_params, silent=args.silent, executor=args.executor)
