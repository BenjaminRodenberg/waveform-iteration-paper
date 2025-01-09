import pandas as pd
from pathlib import Path
import uuid
import argparse

import datetime

from prepesthel.participant import Participant, Participants
from prepesthel.runner import run
from prepesthel.io import Results

default_precice_config_params = {
    'max_used_iterations': 10,
    'time_windows_reused': 5,
}

def postproc(participants: Participants, precice_config_params=None):
    print(f"{datetime.datetime.now()}: Postprocessing...")

    time_window_size = precice_config_params['time_window_size']
    summary = {"time window size": time_window_size}
    for participant in participants.values():
        # store iterations
        df = pd.read_csv(participant.root / f"precice-{participant.name}-iterations.log",delim_whitespace=True)
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
        'waveform_degree': args.waveform_degree,
        'substeps': args.exchange_substeps,
    }

    root_folder = Path(__file__).parent.absolute()

    # Define how participants will be executed here
    participants: Participants = {
        "Dirichlet": Participant(
            "Dirichlet", 
            root_folder / "dirichlet-fenics",
            ["../.venv/bin/python3", "../solver-fenics/heat.py"], 
            ["Dirichlet"], 
            {  # dict with keyword arguments that will be used. Results in python3 script.py param1 ... k1=v1 k2=v2 ...
                '--substeps': None,  # will be defined later
                '--error-tol': 10e10,
                '-g': 'triAcc',
            },
        ),
        "Neumann": Participant(
            "Neumann", 
            root_folder / "neumann-fenics",
            ["../.venv/bin/python3", "../solver-fenics/heat.py"],
            ["Neumann"], 
            {  # dict with keyword arguments that will be used. Results in python3 script.py param1 ... k1=v1 k2=v2 ...
                '--substeps': None,  # will be defined later
                '--error-tol': 10e10,
                '-g': 'triAcc',
            },
        ),
    }

    results_file_path = root_folder
    if args.out_filename:  # use file name given by user
        results_file_path = results_file_path / args.out_filename
    else:  # no file name is given. Create UUID for file name
        results_file_path = results_file_path / "convergence-studies" / f"{uuid.uuid4()}.csv"

    results = Results(results_file_path)

    for dt in [5.0, 2.0, 1.0, 0.5, 0.2, 0.1]:
        refinements = {
            "Dirichlet" : [1,3,5],
            "Neumann" : [1,3,5],
        }
        precice_config_params['time_window_size'] = dt
        for refinement_first in refinements["Dirichlet"]:
            participants["Dirichlet"].kwargs['--substeps'] = refinement_first
            for refinement_second in refinements["Neumann"]:
                participants["Neumann"].kwargs['--substeps'] = refinement_second

                run(participants, args.template_path, precice_config_params)
                summary = postproc(participants, precice_config_params)

                results.append(summary)
                results.output_preliminary()

    results.output_final(participants, args, precice_config_params)

