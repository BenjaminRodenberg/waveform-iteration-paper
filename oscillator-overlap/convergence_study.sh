. .venv/bin/activate
# optimal relationship of dts
python3 doConvergenceStudy.py precice-config-template-FP.xml --config optimal_dt.csv -tss runge_kutta_4 generalized_alpha -wd 3 --exchange-substeps -o convergence-studies/optimal_dt_FP.csv
python3 doConvergenceStudy.py precice-config-template-rQN.xml --config optimal_dt.csv -tss runge_kutta_4 generalized_alpha -wd 3 --exchange-substeps -o convergence-studies/optimal_dt_rQN.csv
python3 doConvergenceStudy.py precice-config-template-fQN.xml --config optimal_dt.csv -tss runge_kutta_4 generalized_alpha -wd 3 --exchange-substeps -o convergence-studies/optimal_dt_fQN.csv
# convergence studies like in Fig1 a) - d)
## Fig 1a) Constant Interpolation
python3 doConvergenceStudy.py precice-config-template-FP.xml --config fig1_dts.csv -tss runge_kutta_4 generalized_alpha -wd 0 -o convergence-studies/fig1a.csv
## Fig 1b) Linear Interpolation
python3 doConvergenceStudy.py precice-config-template-FP.xml --config fig1_dts.csv -tss runge_kutta_4 generalized_alpha -wd 1 -o convergence-studies/fig1b.csv
## Fig 1c) Piecewise Linear Interpolation
python3 doConvergenceStudy.py precice-config-template-FP.xml --config fig1_dts.csv -tss runge_kutta_4 generalized_alpha -wd 1 --exchange-substeps -o convergence-studies/fig1c.csv
## Fig 1d) B-spline Interpolation
python3 doConvergenceStudy.py precice-config-template-FP.xml --config fig1_dts.csv -tss runge_kutta_4 generalized_alpha -wd 3 --exchange-substeps -o convergence-studies/fig1d.csv
