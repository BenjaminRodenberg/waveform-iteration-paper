source .venv/bin/activate
# Figure 6.4a)
python3 doConvergenceStudy.py precice-config-template.xml --waveform-degree 0 --experiment poly --time-window-refinements 1 --time-step-refinements 6 --base-time-window-size 1 -o convergence-studies/subcycling_SC_p0_poly.csv
python3 doConvergenceStudy.py precice-config-template.xml --waveform-degree 1 --experiment poly --time-window-refinements 1 --time-step-refinements 6 --base-time-window-size 1 -o convergence-studies/subcycling_SC_p1_poly.csv
python3 doConvergenceStudy.py precice-config-template.xml --exchange-substeps --waveform-degree 1 --experiment poly --time-window-refinements 1 --time-step-refinements 6 --base-time-window-size 1 -o convergence-studies/subcycling_MC_p1_poly.csv
# Figure 6.4b)
python3 doConvergenceStudy.py precice-config-template.xml --waveform-degree 0 --experiment tri --time-window-refinements 1 --time-step-refinements 6 --base-time-window-size 1 -o convergence-studies/subcycling_SC_p0_tri.csv
python3 doConvergenceStudy.py precice-config-template.xml --waveform-degree 1 --experiment tri --time-window-refinements 1 --time-step-refinements 6 --base-time-window-size 1 -o convergence-studies/subcycling_SC_p1_tri.csv
python3 doConvergenceStudy.py precice-config-template.xml --exchange-substeps --waveform-degree 1 --experiment tri --time-window-refinements 1 --time-step-refinements 6 --base-time-window-size 1 -o convergence-studies/subcycling_MC_p1_tri.csv
# Figure 6.5
python3 doConvergenceStudy.py precice-config-template.xml --experiment tri -w 6 -o convergence-studies/highorder_IE_1.csv
python3 doConvergenceStudy.py precice-config-template.xml --experiment tri -w 6 -s 1 -wd 5 -sb 5 5 -dt 0.5 --exchange-substeps -o convergence-studies/highorder_IE_5.csv
python3 doConvergenceStudy.py precice-config-template.xml --experiment tri -w 6 -s 1 -wd 10 -sb 10 10 -dt 1 --exchange-substeps -o convergence-studies/highorder_IE_10.csv
python3 doConvergenceStudy.py precice-config-template.xml --experiment tri -w 6 -tss GaussLegendre2 GaussLegendre2 --exchange-substeps -o convergence-studies/highorder_GL2_1.csv
python3 doConvergenceStudy.py precice-config-template.xml --experiment tri -w 6 -s 1 -wd 5 -sb 5 5 -dt 0.5 -tss GaussLegendre2 GaussLegendre2 --exchange-substeps -o convergence-studies/highorder_GL2_5.csv
python3 doConvergenceStudy.py precice-config-template.xml --experiment tri -w 6 -tss LobattoIIIC3 LobattoIIIC3 --exchange-substeps -o convergence-studies/highorder_LIIIC_1.csv
python3 doConvergenceStudy.py precice-config-template.xml --experiment tri -w 6 -s 1 -wd 10 -sb 10 10 -dt 1 -tss LobattoIIIC3 LobattoIIIC3 --exchange-substeps -o convergence-studies/highorder_LIIIC_10.csv
