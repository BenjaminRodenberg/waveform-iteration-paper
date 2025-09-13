. .venv/bin/activate
# Section 4.1 partitioned oscillator
## Figure 11
python3 doConvergenceStudy.py configs/precice-config-template-FP.xml --silent --executor Github --config configs/fig11_dts.csv -tss runge_kutta_4 generalized_alpha -wd 3 --exchange-substeps -o results/Fig11/data/contour_data.csv
## Figure 10
### constant
python3 doConvergenceStudy.py configs/precice-config-template-FP.xml --config configs/fig10_dts.csv -tss runge_kutta_4 generalized_alpha -wd 0 -o results/Fig10/data/constant.csv
### linear
python3 doConvergenceStudy.py configs/precice-config-template-FP.xml --config configs/fig10_dts.csv -tss runge_kutta_4 generalized_alpha -wd 1 -o results/Fig10/data/linear.csv
### piecewise linear
python3 doConvergenceStudy.py configs/precice-config-template-FP.xml --config configs/fig10_dts.csv -tss runge_kutta_4 generalized_alpha -wd 1 --exchange-substeps -o results/Fig10/data/piecewise_linear.csv
### third-degree B-spline
python3 doConvergenceStudy.py configs/precice-config-template-FP.xml --config configs/fig10_dts.csv -tss runge_kutta_4 generalized_alpha -wd 3 --exchange-substeps -o results/Fig10/data/third_degree_b-spline.csv
## Table 1 optimal relationship of dts
python3 doConvergenceStudy.py configs/precice-config-template-FP.xml --config configs/tab1_dts.csv -tss runge_kutta_4 generalized_alpha -wd 3 --exchange-substeps -o results/Tab1/data/FP.csv
python3 doConvergenceStudy.py configs/precice-config-template-rQN.xml --config configs/tab1_dts.csv -tss runge_kutta_4 generalized_alpha -wd 3 --exchange-substeps -o results/Tab1/data/rQN.csv
python3 doConvergenceStudy.py configs/precice-config-template-fQN.xml --config configs/tab1_dts.csv -tss runge_kutta_4 generalized_alpha -wd 3 --exchange-substeps -o results/Tab1/data/rQN.csv
