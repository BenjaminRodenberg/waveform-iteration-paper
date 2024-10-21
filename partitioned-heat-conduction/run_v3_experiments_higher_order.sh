source ./dirichlet-fenics/.venv/bin/activate

python3 doConvergenceStudy.py precice-config-template.xml --experiment tri -w 6
python3 doConvergenceStudy.py precice-config-template.xml --experiment tri -w 6 -s 1 -wd 5 -sb 5 5 -dt 0.5 --exchange-substeps
python3 doConvergenceStudy.py precice-config-template.xml --experiment tri -w 6 -s 1 -wd 10 -sb 10 10 -dt 1 --exchange-substeps
python3 doConvergenceStudy.py precice-config-template.xml --experiment tri -w 6 -tss GaussLegendre2 GaussLegendre2 --exchange-substeps
python3 doConvergenceStudy.py precice-config-template.xml --experiment tri -w 6 -s 1 -wd 5 -sb 5 5 -dt 0.5 -tss GaussLegendre2 GaussLegendre2 --exchange-substeps
python3 doConvergenceStudy.py precice-config-template.xml --experiment tri -w 5 -s 1 -wd 20 -sb 20 20 -dt 1 -tss GaussLegendre8 GaussLegendre8 --exchange-substeps
python3 doConvergenceStudy.py precice-config-template.xml --experiment tri -w 6 -tss LobattoIIIC3 LobattoIIIC3 --exchange-substeps
python3 doConvergenceStudy.py precice-config-template.xml --experiment tri -w 6 -s 1 -wd 10 -sb 10 10 -dt 1 -tss LobattoIIIC3 LobattoIIIC3 --exchange-substeps
