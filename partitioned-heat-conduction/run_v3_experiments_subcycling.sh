source ./dirichlet-fenics/.venv/bin/activate

python3 doConvergenceStudy.py precice-config-template.xml --experiment tri -w 6
python3 doConvergenceStudy.py precice-config-template.xml --experiment tri -w 6 -s 1 -sb 5 5 -dt 0.5
python3 doConvergenceStudy.py precice-config-template.xml --experiment tri -w 6 -s 1 -sb 10 10 -dt 1
