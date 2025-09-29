from jinja2 import Environment, select_autoescape, FileSystemLoader
import pandas as pd
from pathlib import Path
import uuid
import argparse

import datetime

from prepesthel.participant import Participant, Participants
from prepesthel.runner import run
from prepesthel.io import Results, Executors

def render_control_dict(template_path, out, time_step_size):
    root = Path()
    env = Environment(
        loader=FileSystemLoader(root)
    )

    control_dict_template = env.get_template(str(template_path.relative_to(root.resolve())))

    with open(out, "w") as file:
        file.write(control_dict_template.render({'deltaT': time_step_size}))


def postproc(participants: Participants, precice_config_params=None):
    print(f"{datetime.datetime.now()}: Postprocessing...")

    time_window_size = precice_config_params['time_window_size']
    summary = {
        "time window size": time_window_size,
        "substeps": precice_config_params['substeps'],
        "waveform degree": precice_config_params['waveform_degree'],
        "reduced": precice_config_params['reduced'],
        "acceleration": precice_config_params['acceleration'],
    }

    for participant in participants.values():
        # store iterations
        df = pd.read_csv(participant.root / f"precice-{participant.name}-iterations.log",sep="\s+")
        summary[f"substeps {participant.name}"] = participant.substeps
        summary[f"time step size {participant.name}"] = time_window_size / participant.substeps
        summary["avg(iterations / window)"] = df["Iterations"].mean()
        summary["max(iterations / window)"] = df["Iterations"].max()
        summary["no. QN"] = df["Iterations"].sum()

    print(f"{datetime.datetime.now()}: Done.")

    return summary


if __name__ == "__main__":
    n_supported_participants = 2

    parser = argparse.ArgumentParser(description="Solving perpendicular flap")
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
        "time_config",
        help="Path to a CSV defining the time window and time step sizes of the individual experiments",
        type=str)
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
        'max_time': None,  # will be defined later
        'waveform_degree': None,  # will be defined later
        'reduced': None,  # will be defined later
        'substeps': None,  # will be defined later
    }

    root_folder = Path(__file__).parent.absolute()

    # Define how participants will be executed here
    participants: Participants = {
        "Fluid": Participant("Fluid", root_folder / "fluid-openfoam", ["./run.sh"], [], {}),
        "Solid": Participant("Solid", root_folder / "solid-fenics", [".venv/bin/python3"], ["solid.py"], {'--n-substeps': None}),
    }

    if len(participants) != n_supported_participants:
        raise Exception(f"Currently only supports coupling of {n_supported_participants} participants")
    
    # Use configuration provided in csv file
    config_path = Path(args.time_config)
    time_step_config = pd.read_csv(config_path, comment='#')
        
    results_file_path = root_folder
    if args.out_filename:  # use file name given by user
        results_file_path = results_file_path / args.out_filename
    else:  # no file name is given. Create UUID for file name
        results_file_path = results_file_path / "convergence-studies" / f"{uuid.uuid4()}.csv"

    results = Results(results_file_path)
   
    watchpoint_folder = results_file_path.parent / results_file_path.stem  # use path without .csv as folder for watchpoints
    watchpoint_folder.mkdir(parents=False, exist_ok=False)

    for _, experiment_setup in time_step_config.iterrows():
        precice_config_params['time_window_size'] = experiment_setup['time window size']
        precice_config_params['max_time'] = experiment_setup['max time']
        precice_config_params['waveform_degree'] = experiment_setup['waveform degree']
        precice_config_params['reduced'] = experiment_setup['reduced']
        precice_config_params['substeps'] = experiment_setup['substeps']
        precice_config_params['acceleration'] = "qn"
        
        # Vary number of substeps for OpenFOAM Fluid participant by modifying fluid-openfoam/system/controlDict
        p = participants["Fluid"]
        render_control_dict(p.root / 'system' / 'controlDict-template', p.root / 'system' / 'controlDict',  experiment_setup[f'time step size {p.name}'])
        substeps = round(experiment_setup['time window size'] / experiment_setup[f'time step size {p.name}'])
        p.substeps = substeps  # store substeps here for postprocessing
        # Vary number of substeps for FEniCS Solid participant via kwargs
        p = participants["Solid"]
        substeps = round(experiment_setup['time window size'] / experiment_setup[f'time step size {p.name}'])
        p.kwargs['--n-substeps'] = substeps
        p.substeps = substeps  # store substeps here for postprocessing

        run(participants, args.template_path, precice_config_params)
        summary = postproc(participants, precice_config_params)

        results.append(summary)
        results.output_preliminary(silent=args.silent)

        # move watchpoint file to watchpoint folder; label with id given in experiment_setup
        (participants["Solid"].root / "precice-Solid-watchpoint-Flap-Tip.log").rename(watchpoint_folder / f"watchpoint_{experiment_setup['id']}")

        # move all iterations files to experiment folder
        ## create some folders
        experiment_folder = watchpoint_folder / experiment_setup['id']
        experiment_folder.mkdir(parents=False, exist_ok=False)
        ## copy all relevant files
        for f in [participants["Solid"].root / "precice-Solid-iterations.log", 
                  participants["Solid"].root / "precice-Solid-convergence.log",
                  participants["Fluid"].root / "precice-Fluid-iterations.log"]:
            f.rename(experiment_folder / f.name)
    
    results.output_final(participants, args, precice_config_params, silent=args.silent, executor=args.executor)