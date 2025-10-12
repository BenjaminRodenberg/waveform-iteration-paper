. .venv/bin/activate
# Section 4.2 partitioned heat conduction

## Figure 13
python3 doConvergenceStudyMonolithic.py --experiment sincos -s 6 -dt 0.2 -tss BackwardEuler -o results/Fig13/data/IE_mono.csv
python3 doConvergenceStudy.py precice-config.xml.jinja2 --experiment sincos -w 6 -s 1 -wd 3 -sb 5 5 -dt 1 -tss BackwardEuler BackwardEuler --exchange-substeps -o results/Fig13/data/IE_3.csv
python3 doConvergenceStudy.py precice-config.xml.jinja2 --experiment sincos -w 6 -s 1 -wd 2 -sb 5 5 -dt 1 -tss GaussLegendre2 GaussLegendre2 --exchange-substeps -o results/Fig13/data/GL2_2.csv
python3 doConvergenceStudy.py precice-config.xml.jinja2 --experiment sincos -w 6 -s 1 -wd 3 -sb 5 5 -dt 1 -tss GaussLegendre2 GaussLegendre2 --exchange-substeps -o results/Fig13/data/GL2_3.csv
python3 doConvergenceStudyMonolithic.py --experiment sincos -s 6 -dt 0.2 -tss GaussLegendre2 -o results/Fig13/data/GL2_mono.csv
python3 doConvergenceStudy.py precice-config.xml.jinja2 --experiment sincos -w 6 -s 1 -wd 5 -sb 5 5 -dt 1 -tss GaussLegendre2 GaussLegendre2 --exchange-substeps -o results/Fig13/data/GL2_5.csv
python3 doConvergenceStudy.py precice-config.xml.jinja2 --experiment sincos -w 6 -s 1 -wd 3 -sb 5 5 -dt 1 -tss GaussLegendre3 GaussLegendre3 --exchange-substeps -o results/Fig13/data/GL3_3.csv
python3 doConvergenceStudy.py precice-config.xml.jinja2 --experiment sincos -w 6 -s 1 -wd 5 -sb 5 5 -dt 1 -tss GaussLegendre3 GaussLegendre3 --exchange-substeps -o results/Fig13/data/GL3_5.csv
python3 doConvergenceStudyMonolithic.py --experiment sincos -s 6 -dt 0.2 -tss GaussLegendre3 -o results/Fig13/data/GL3_mono.csv

## Figure 13 extra LIIIC3
python3 doConvergenceStudyMonolithic.py --experiment sincos -s 6 -dt 0.2 -tss LobattoIIIC3 -o results/Fig13extra/data/LIIIC3_mono.csv
python3 doConvergenceStudy.py precice-config.xml.jinja2 --experiment sincos -w 6 -s 1 -wd 2 -sb 5 5 -dt 1 -tss LobattoIIIC3 LobattoIIIC3 --exchange-substeps -o results/Fig13extra/data/LIIIC3_2.csv
python3 doConvergenceStudy.py precice-config.xml.jinja2 --experiment sincos -w 6 -s 1 -wd 3 -sb 5 5 -dt 1 -tss LobattoIIIC3 LobattoIIIC3 --exchange-substeps -o results/Fig13extra/data/LIIIC3_3.csv
python3 doConvergenceStudy.py precice-config.xml.jinja2 --experiment sincos -w 6 -s 1 -wd 5 -sb 5 5 -dt 1 -tss LobattoIIIC3 LobattoIIIC3 --exchange-substeps -o results/Fig13extra/data/LIIIC3_5.csv
