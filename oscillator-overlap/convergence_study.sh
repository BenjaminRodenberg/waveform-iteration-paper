. .venv/bin/activate
# Figure 6.1
python3 doConvergenceStudy.py precice-config-template.xml -tss runge_kutta_4 generalized_alpha -wd 3 -dt 0.05 -sb 4 4 -s 8 -sf 1 2 -w 1 -o convergence-studies/subcycling_rk4_ga.csv
python3 doConvergenceStudy.py precice-config-template.xml -tss runge_kutta_4 runge_kutta_4 -wd 3 -dt 0.05 -sb 4 4 -s 8 -sf 1 2 -w 1 -o convergence-studies/subcycling_rk4_rk4.csv
# Figure 6.2a
python3 doConvergenceStudy.py precice-config-template.xml --config convergence-studies/fig6_2a_config.csv -tss runge_kutta_4 generalized_alpha -wd 3 -o convergence-studies/contour_data.csv
# Figure 6.2b
python3 doConvergenceStudy.py precice-config-template.xml -tss runge_kutta_4 generalized_alpha -dt 0.2 -wd 3 -sb 4 4 -o convergence-studies/compensation_S_2_4.csv
python3 doConvergenceStudy.py precice-config-template.xml -tss runge_kutta_4 generalized_alpha -dt 0.2 -wd 3 -sb 4 8 -o convergence-studies/compensation_S_2_8.csv
python3 doConvergenceStudy.py precice-config-template.xml -tss runge_kutta_4 generalized_alpha -dt 0.2 -wd 3 -sb 4 16 -o convergence-studies/compensation_S_2_16.csv
python3 doConvergenceStudy.py precice-config-template.xml -tss runge_kutta_4 generalized_alpha -dt 0.2 -wd 3 -sb 4 32 -o convergence-studies/compensation_S_2_32.csv
python3 doConvergenceStudy.py precice-config-template.xml -tss runge_kutta_4 generalized_alpha -dt 0.2 -wd 3 -sb 4 64 -o convergence-studies/compensation_S_2_64.csv
python3 doConvergenceStudy.py precice-config-template.xml -tss runge_kutta_4 generalized_alpha -dt 0.2 -wd 3 -sb 4 128 -o convergence-studies/compensation_S_2_128.csv
python3 doConvergenceStudy.py precice-config-template.xml -tss runge_kutta_4 generalized_alpha -dt 0.2 -wd 3 -sb 4 256 -o convergence-studies/compensation_S_2_256.csv
