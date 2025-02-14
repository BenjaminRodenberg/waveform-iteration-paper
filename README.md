# Test cases from the dissertation of Benjamin Rodenberg

This repository contains modified versions of the tutorial cases from https://github.com/precice/tutorials/releases/tag/v202404.0. These tutorials acted as test cases for the PhD thesis "Flexible and robust time stepping forpartitioned multiphysics" of Benjamin Rodenberg in Chapter 6 "Test cases". The folders in this repository are related to the following (sub-)sections of the thesis:

* `oscillator-overlap`: 6.1 Oscillator problem: 
    * Refer to `oscillator-overlap/convergence_studies.sh` for the experiments shown in Figures 6.1 and 6.2.
    * **TODO** Refer to `oscillator-overlap/energy_conservation.sh` for the experiments shown in Figure 6.3.
* `partitioned-heat-conduction`: 6.2 Partitioned heat conduction
    * Refer to `partitioned-heat-conduction/convergence_study.sh` for the experiments shown in Figures 6.4 and 6.5.
    * Refer to `partitioned-heat-conduction/acceleration_study.sh` for the experiments shown in Table 6.1.
* `perpendicular-flap`: 6.3.1 Perpendicular flap
    * Refer to `perpendicular-flap/do_studies.sh` for the experiments shown in Figures 6.6 and 6.7.
* `turek-hron-fsi3`: 6.3.2 FSI3 benchmark
    * **TODO** Refer to `turek-hron-fsi3/do_studies.sh` for the experiments shown in Figure 6.8.

Please consider citing the preCICE distribution[^1] or Benjamin Rodenberg's PhD thesis[^2] if you find these tutorial cases useful.

## Dependencies

The preCICE distribution version v2404.0 [^1] should provide a good basis for running the experiments provided in this repository. If available I used suggest to use the latest versions of preCICE, respectively adapters. The experiments are known to run as expected on a system with the following specification:

### preCICE components

* preCICE `0faa86d` (temporary version, https://github.com/precice/precice/pull/2194/commits/0faa86de27db6f1e955af377b9257db5ff48133b, features will be released in upcoming v3.2.0 of preCICE); built with default CMake configuration.
* pyprecice `3.1.2` (refer to requirements.txt of the respective case)
* FEniCS adapter `2.2.0` (refer to requirements.txt of the respective case)
* OpenFOAM adapter `1.3.1` (https://github.com/precice/openfoam-adapter/releases/tag/v1.3.1)
* deal.II adapter `02c5d18` (https://github.com/precice/dealii-adapter/commit/02c5d1849d1b1746de389a3373f08441b7df64f5; unverified). Use `f283a0f` as fall-back if necessary.

### OS and other dependencies

* Ubuntu `24.04`
* Additional python packages (according to requirements.txt of the respective case)
* FEniCS `2019.2.0.64.dev0` (installed from FEniCS PPA https://launchpad.net/~fenics-packages/+archive/ubuntu/fenics; compare version provided by `python3 -c "import dolfin;print(dolfin.__version__)`")
* OpenFOAM `2406`
* deal.II `version 9.7.0-pre, shortrev d0584bbf39`


[^1]: Chen, Jun; Chourdakis, Gerasimos; Desai, Ishaan; Homs-Pons, Carme; Rodenberg, Benjamin; Schneider, David; Simonis, Frédéric; Uekermann, Benjamin; Davis, Kyle; Jaust, Alexander; Kelm, Mathis; Kotarsky, Niklas; Kschidock, Helena; Mishra, Durganshu; Mühlhäußer, Markus; Schrader, Timo Pierre; Schulte, Miriam; Seitz, Valentin; Signorelli, Joseph; van Zwieten, Gertjan; Vinnitchenko, Niklas; Vladimirova, Tina; Willeke, Leonard; Zonta, Elia. *preCICE Distribution Version v2404.0*. DaRUS, 2024, V1. https://doi.org/10.18419/darus-4167.
[^2]: Rodenberg, Benjamin. *Flexible and robust time stepping for partitioned multiphysics*. Technical University of Munich, 2025. Unpublished manuscript. Available at: https://doi.org/**TODO**.
