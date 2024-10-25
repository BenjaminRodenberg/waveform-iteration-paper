source ./dirichlet-fenics/.venv/bin/activate

python3 doConvergenceStudy.py precice-config-template.xml --waveform-degree 0 --experiment poly1 -w 6 -s 1 -sb 1 1 -dt 1
python3 doConvergenceStudy.py precice-config-template.xml --waveform-degree 0 --experiment poly1 -w 1 -s 6 -sb 1 1 -dt 1
python3 doConvergenceStudy.py precice-config-template.xml --experiment poly1 -w 6 -s 1 -sb 1 1 -dt 1
python3 doConvergenceStudy.py precice-config-template.xml --experiment poly1 -w 1 -s 6 -sb 1 1 -dt 1
python3 doConvergenceStudy.py precice-config-template.xml --exchange-substeps --experiment poly1 -w 6 -s 1 -sb 1 1 -dt 1
python3 doConvergenceStudy.py precice-config-template.xml --exchange-substeps --experiment poly1 -w 1 -s 6 -sb 1 1 -dt 1
python3 doConvergenceStudy.py precice-config-template.xml --waveform-degree 0 --experiment tri -w 6 -s 1 -sb 1 1 -dt 1
python3 doConvergenceStudy.py precice-config-template.xml --waveform-degree 0 --experiment tri -w 1 -s 6 -sb 1 1 -dt 1
python3 doConvergenceStudy.py precice-config-template.xml --experiment tri -w 6 -s 1 -sb 1 1 -dt 1
python3 doConvergenceStudy.py precice-config-template.xml --experiment tri -w 1 -s 6 -sb 1 1 -dt 1
python3 doConvergenceStudy.py precice-config-template.xml --exchange-substeps --experiment tri -w 6 -s 1 -sb 1 1 -dt 1
python3 doConvergenceStudy.py precice-config-template.xml --exchange-substeps --experiment tri -w 1 -s 6 -sb 1 1 -dt 1
