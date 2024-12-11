. .venv/bin/activate
# Figure 6.1
python3 doConvergenceStudy.py precice-config-template.xml -tss runge_kutta_4 generalized_alpha -wd 3 -dt 0.05 -sb 4 4 -s 8 -sf 1 2 -w 1 -o convergence-studies/subcycling_rk4_ga.csv
python3 doConvergenceStudy.py precice-config-template.xml -tss runge_kutta_4 runge_kutta_4 -wd 3 -dt 0.05 -sb 4 4 -s 8 -sf 1 2 -w 1  -o convergence-studies/subcycling_rk4_rk4.csv
# Figure 6.2
# TODO