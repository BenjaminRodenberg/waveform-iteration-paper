source .venv/bin/activate
# Table 6.1
python3 doAccelerationStudy.py precice-config-rQNWI-template.xml -o acceleration-studies/QN-SC.csv
python3 doAccelerationStudy.py --exchange-substeps precice-config-rQNWI-template.xml -o acceleration-studies/rQN-WI.csv
