import pandas as pd
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

import argparse

parser = argparse.ArgumentParser(description="Create LaTeX code for table summarizing average iterations")
parser.add_argument(
    "file",
    type=Path,
    help="Path to csv file for experiment."
)
args = parser.parse_args()

experiment_file = args.file

df = pd.read_csv(experiment_file, comment='#', sep=',')

data = {
    '$\\Delta t$': [],
    '$e_A$': [],
    '$e_B$': [],
    'Avg. its.': [],
}

for r in df.to_dict(orient='records'):
    time_window = round(r['time window size'], ndigits=10)
    time_step_1 = round(r['time step size Mass-Left'], ndigits=10)
    time_step_2 = round(r['time step size Mass-Right'], ndigits=10)
    its_df = pd.read_csv(experiment_file.parent / experiment_file.stem / f'{time_window}_{time_step_1}_{time_step_2}' / 'precice-Mass-Left-iterations.log', delimiter=r"\s+")

    data['$\\Delta t$'].append(time_window)
    data['$e_A$'].append('%.2E'%r['error Mass-Left'])
    data['$e_B$'].append('%.2E'%r['error Mass-Right'])
    data['Avg. its.'].append(its_df['Iterations'].mean())

# Load the Jinja2 template from the file system
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('table-template.tex.jinja2')

df = pd.DataFrame(data)

# Get the column labels and data for Jinja2
columns = df.columns.tolist()  # Get column names
data_rows = df.values.tolist()  # Get the data as a list of rows

# Render LaTeX table using the custom Jinja2 template
latex_code = template.render(columns=columns, data=data_rows, acc_scheme=experiment_file.stem)

# Write the LaTeX code to file
with open(experiment_file.stem + '.tex', 'w') as f:
    f.write(latex_code)
