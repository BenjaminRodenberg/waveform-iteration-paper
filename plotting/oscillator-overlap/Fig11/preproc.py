import argparse
import pandas as pd
from pathlib import Path

parser = argparse.ArgumentParser(description="Extract contour lines for levels from given contour_data.csv")
parser.add_argument(
    "cdata",
    type=Path,
    help="Path to 'contour_data.csv'."
)
args = parser.parse_args()

outdir = args.cdata.parent

parser = argparse.ArgumentParser()

times = pd.DataFrame(columns=['x', 'y', 'z', 'w'])

df = pd.read_csv(args.cdata, sep=',', comment='#')
for l in df.iterrows():
    times.loc[-1] = [
        l[1]['time step size Mass-Right'],
        l[1]['time step size Mass-Left'],
        max([l[1]['error Mass-Left'],l[1]['error Mass-Right']]),
        l[1]['time window size']
    ]
    times.index += 1
    times = times.sort_index()

import numpy as np
import scipy.interpolate as interp

interpolator = interp.CloughTocher2DInterpolator(np.array([times['x'],times['y']]).T, times['z'])

times = times.sort_values(['x', 'y'])
times = times.set_index(['x','y'])

from matplotlib import pyplot as plt

import numpy as np

X, Y = np.meshgrid(np.logspace(np.log10(1.25*1e-5), np.log10(1e-1)),
                   np.logspace(np.log10(1e-3), np.log10(1e-1)))
Z = interpolator(X,Y)

# simple cost model: RK4 requires 4 f evaluations * 1/Y steps; GA requires 2(?) f evaluations * 1/X steps
C = 2/(X) + 4/(Y)

from matplotlib import ticker

def fmt(x):
    return "{:.0E}".format(x)

CS = plt.contour(X,Y,Z,np.array([1e-7,1e-6,1e-5,1e-4,1e-3]),locator=ticker.LogLocator())

for c_level, c_line in zip(CS.levels, CS.allsegs):
    n_pts = len(c_line[0][:,0])
    d = {'id': range(n_pts), 'c_level':n_pts*[c_level], 'c_line_x':c_line[0][:,0], 'c_line_y':c_line[0][:,1]}
    df_contours = pd.DataFrame(d)
    df_contours = df_contours.set_index("id")
    df_contours.to_csv(outdir / f"contour_{c_level}.csv", sep=';')

times_reduced = times.iloc[times.index.get_level_values('y') >= 1e-3]
times_reduced.to_csv(outdir / "times_reduced.csv", sep=';')