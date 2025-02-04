# Figure 6.8
cp precice-config-fenics.xml precice-config.xml
cp fluid-openfoam/system/preciceDict-fenics fluid-openfoam/system/preciceDict
(cd ./solid-fenics && ./run_legacy.sh) & (cd ./fluid-openfoam && ./run.sh)
cp ./solid-fenics/precice-Solid-watchpoint-Flap-Tip.log ./studies/precice-Solid-watchpoint-Flap-Tip-legacy.log

cp precice-config-fenics.xml precice-config.xml
cp fluid-openfoam/system/preciceDict-fenics fluid-openfoam/system/preciceDict
(cd ./solid-fenics && ./run_WI.sh) & (cd ./fluid-openfoam && ./run.sh)
cp ./solid-fenics/precice-Solid-watchpoint-Flap-Tip.log ./studies/precice-Solid-watchpoint-Flap-Tip-WI.log

cp precice-config-dealii.xml precice-config.xml
cp fluid-openfoam/system/preciceDict-dealii fluid-openfoam/system/preciceDict
(cd ./solid-dealii && ./run.sh) & (cd ./fluid-openfoam && ./run.sh)
cp ./solid-dealii/precice-Solid-watchpoint-Flap-Tip.log ./studies/precice-Solid-watchpoint-Flap-Tip-nonlin.log