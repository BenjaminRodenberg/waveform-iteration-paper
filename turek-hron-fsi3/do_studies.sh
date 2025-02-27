# Figure 6.8
./prep_fenics.sh
(cd ./solid-fenics && ./run_legacy.sh) & (cd ./fluid-openfoam && ./run.sh)
cp ./solid-fenics/precice-Solid-watchpoint-Flap-Tip.log ./studies/precice-Solid-watchpoint-Flap-Tip-legacy.log

./prep_fenics.sh
(cd ./solid-fenics && ./run_WI.sh) & (cd ./fluid-openfoam && ./run.sh)
cp ./solid-fenics/precice-Solid-watchpoint-Flap-Tip.log ./studies/precice-Solid-watchpoint-Flap-Tip-WI.log

./prep_dealii.sh
(cd ./solid-dealii && ./run.sh) & (cd ./fluid-openfoam && ./run.sh)
cp ./solid-dealii/precice-Solid-watchpoint-Flap-Tip.log ./studies/precice-Solid-watchpoint-Flap-Tip-nonlin.log
