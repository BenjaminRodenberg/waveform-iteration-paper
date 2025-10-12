import pandas as pd
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

import argparse

parser = argparse.ArgumentParser(description="Insert data into table in LaTeX code")
parser.add_argument(
    "file",
    type=Path,
    help="Path to csv file for experiment."
)
args = parser.parse_args()

experiment_file = args.file

df = pd.read_csv(experiment_file, comment='#', sep=',')

data = {
    'id': [],
    '$\\Delta t$': [],
    '$\\delta t_F$': [],
    '$\\delta t_S$': [],
    'Avg. its.': [],
}

for r in df.to_dict(orient='records'):
    time_window = round(r['time window size'], ndigits=10)
    time_step_1 = round(r['time step size Fluid'], ndigits=10)
    substeps_1 = r['substeps Fluid']
    time_step_2 = round(r['time step size Solid'], ndigits=10)
    substeps_2 = r['substeps Solid']

    if time_window < 0.1:
        experiment_id = 'REF'
    else:
        experiment_id = f'MC_{substeps_1}_{substeps_2}'

    its_df = pd.read_csv(experiment_file.parent / experiment_file.stem / experiment_id / 'precice-Fluid-iterations.log', delimiter=r"\s+")

    data['id'].append(f'\\ref{{plot:{experiment_id}}}')
    data['$\\Delta t$'].append(time_window)
    data['$\\delta t_F$'].append(time_step_1)
    data['$\\delta t_S$'].append(time_step_2)
    data['Avg. its.'].append('{0:0.2f}'.format(its_df['Iterations'].mean()))

# Load the Jinja2 template from the file system
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('tikzcode.tex.jinja2')

df = pd.DataFrame(data)

# Get the column labels and data for Jinja2
columns = df.columns.tolist()  # Get column names
data_rows = df.values.tolist()  # Get the data as a list of rows

# Render LaTeX table using the custom Jinja2 template
latex_code = template.render(columns=columns, data=data_rows, acc_scheme=experiment_file.stem)

# Write the LaTeX code to file
with open('tikzcode.tex', 'w') as f:
    f.write(latex_code)
