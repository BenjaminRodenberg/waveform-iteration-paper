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

linear_dts = []
linear_refs = {}
linear_its = {}
wi_dts = []
wi_refs = {}
wi_its = {}

for r in df.to_dict(orient='records'):
    dt = r['time window size']

    is_ref = dt == r['time step size Fluid'] and dt == r['time step size Solid']  # is reference experiment
    substeps_solid = r['substeps Solid']

    if is_ref:
        experiment_id = 'REF'
        linear_dts.append(dt)
        linear_refs[dt] = experiment_id
        wi_dts.append(dt)
        wi_refs[dt] = experiment_id
    elif r['substeps']:
        experiment_id = f'MC_S{substeps_solid}_rQNWI'
        wi_dts.append(dt)
        wi_refs[dt] = experiment_id
    elif not r['substeps']:
        experiment_id = f'SC_S{substeps_solid}'
        linear_dts.append(dt)
        linear_refs[dt] = experiment_id

    its_df = pd.read_csv(experiment_file.parent / experiment_file.stem / experiment_id / 'precice-Fluid-iterations.log', delimiter=r"\s+")

    its = '{0:0.2f}'.format(its_df['Iterations'].mean())

    if is_ref:
        wi_its[dt] = its
        linear_its[dt] = its
    elif r['substeps']:
        wi_its[dt] = its
    elif not r['substeps']:
        linear_its[dt] = its

# Load the Jinja2 template from the file system
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('tikzcode.tex.jinja2')

df = pd.DataFrame(data)

# Get the column labels and data for Jinja2
columns = df.columns.tolist()  # Get column names
data_rows = df.values.tolist()  # Get the data as a list of rows

# Render LaTeX table using the custom Jinja2 template
data = []
for dt in wi_dts:
    data.append(
        {
            'dt':dt,
            'linear_ref':linear_refs[dt],
            'linear_its':linear_its[dt],
            'wi_ref': wi_refs[dt],
            'wi_its': wi_its[dt],
        }
    )

print(data)

latex_code = template.render(data=data,
                             valid_refs=['REF'] +
                             [f'MC_S{it}_rQNWI' for it in [10,100,500]] +
                             [f'SC_S{it}' for it in [10,100,500]])

# Write the LaTeX code to file
with open('tikzcode.tex', 'w') as f:
    f.write(latex_code)
