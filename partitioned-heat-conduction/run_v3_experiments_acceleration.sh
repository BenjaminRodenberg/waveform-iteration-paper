source ./dirichlet-fenics/.venv/bin/activate

python3 doAccelerationStudy.py precice-config-relWI-template.xml
python3 doAccelerationStudy.py --exchange-substeps precice-config-relWI-template.xml
python3 doAccelerationStudy.py precice-config-rQNWI-template.xml
python3 doAccelerationStudy.py --exchange-substeps precice-config-rQNWI-template.xml
