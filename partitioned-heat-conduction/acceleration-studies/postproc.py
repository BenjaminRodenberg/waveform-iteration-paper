import pandas as pd

import argparse

parser = argparse.ArgumentParser(description="Postprocess output into latex table for publication")
parser.add_argument(
    "file_path",
    help="file to be parsed",
    type=str)
parser.add_argument(
    "-a",
    "--acceleration",
    choices=("QN", "rQN", "rel"),
    type=str,
    required=True,
)
parser.add_argument(
    "-s",
    "--scheme",
    choices=("SC", "WI"),
    type=str,
    required=True,
)
args = parser.parse_args()

df = pd.read_csv(args.file_path, comment='#')

acceleration_method = f'{args.acceleration}-{args.scheme}'
waveform_degree = 1
coupling_method = f'{args.scheme}'

latex_code = ''

dTs = df['time window size'].unique()
dTs.sort()
lines = []
line = f'{acceleration_method} | $\\Delta t$ & '+' & '.join(map('${0:.2f}$'.format, dTs.tolist()[::-1]))
line += '\\\\'
line += ' \\midrule'
lines.append(line)

for s_dirichlet in [1,3,5]:
    for s_neumann in [1,3,5]:
        line = []
        line.append(f"$\\text{{{coupling_method}}}\\left({s_dirichlet},{s_neumann};{waveform_degree}\\right)$")
        for dT in dTs[::-1]:
            line.append(f"${df[(df['substeps Dirichlet'] == s_dirichlet) & (df['substeps Neumann'] == s_neumann) & (df['time window size'] == dT)]['avg(iterations / window)'].max():.2f}$")
        line = ' & '.join(line)
        line += '\\\\'
        lines.append(line)

for line in lines:
    print(line)