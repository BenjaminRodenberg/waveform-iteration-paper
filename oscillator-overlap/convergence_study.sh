. .venv/bin/activate
# optimal relationship of dts
python3 doConvergenceStudy.py precice-config-template-FP.xml --config optimal_dt.csv -tss runge_kutta_4 generalized_alpha -wd 3 --exchange-substeps -o convergence-studies/optimal_dt_FP.csv
python3 doConvergenceStudy.py precice-config-template-rQN.xml --config optimal_dt.csv -tss runge_kutta_4 generalized_alpha -wd 3 --exchange-substeps -o convergence-studies/optimal_dt_rQN.csv
python3 doConvergenceStudy.py precice-config-template-fQN.xml --config optimal_dt.csv -tss runge_kutta_4 generalized_alpha -wd 3 --exchange-substeps -o convergence-studies/optimal_dt_fQN.csv
