# Test cases from the dissertation of Benjamin Rodenberg

This repository contains modified versions of the tutorial cases from https://github.com/precice/tutorials/releases/tag/v202404.0. These tutorials acted as test cases for the PhD thesis "Flexible and robust time stepping for partitioned multiphysics" of Benjamin Rodenberg in Chapter 6 "Test cases". The folders in this repository are related to the following (sub-)sections of the thesis:

* `oscillator-overlap`: 6.1 Oscillator problem: 
    * Refer to `oscillator-overlap/convergence_studies.sh` for the experiments shown in Figures 6.1 and 6.2.
* `partitioned-heat-conduction`: 6.2 Partitioned heat conduction
    * Refer to `partitioned-heat-conduction/convergence_study.sh` for the experiments shown in Figures 6.4 and 6.5.
    * Refer to `partitioned-heat-conduction/acceleration_study.sh` for the experiments shown in Table 6.1.
* `perpendicular-flap`: 6.3.1 Perpendicular flap
    * Refer to `perpendicular-flap/do_studies.sh` for the experiments shown in Figures 6.6 and 6.7.
* `turek-hron-fsi3`: 6.3.2 FSI3 benchmark
    * Refer to `turek-hron-fsi3/do_studies.sh` for the experiments shown in Figure 6.8.

Please consider citing the preCICE distribution[^1] or Benjamin Rodenberg's PhD thesis[^2] if you find these tutorial cases useful.

You can use the workflows under `.github/workflows` to run the different tests cases via workflow dispatch.

## Dependencies

The preCICE distribution version v2404.0 [^1] should provide a good basis for running the experiments provided in this repository. However, I suggest to use the latest versions of preCICE, respectively adapters. The experiments are known to run as expected on a system with the following specification:

### preCICE components

* preCICE [`8b5115e`](https://github.com/precice/precice/commit/8b5115ee689a71f4d8f473cbe633a3ff8d642050) (temporary version, features will be released in upcoming `v3.2.0` of preCICE); built with default CMake configuration.
* pyprecice [`3.1.2`](https://github.com/precice/python-bindings/releases/tag/v3.1.2) (automatically installed via `requirements.txt` of the respective case)
* FEniCS adapter [`2.2.0`](https://github.com/precice/fenics-adapter/releases/tag/v2.2.0) (automatically installed via `requirements.txt` of the respective case)
* OpenFOAM adapter [`1.3.1`](https://github.com/precice/openfoam-adapter/releases/tag/v1.3.1)
* deal.II adapter [`4c6d092`](https://github.com/precice/dealii-adapter/commit/4c6d092c60c750478b08cfac25da1ff174c2d6f5)

### OS and other dependencies

* Ubuntu `24.04`
* Additional python packages (automatically installed via `requirements.txt` of the respective case)
* FEniCS `2019.2.0.64.dev0` (installed from FEniCS PPA https://launchpad.net/~fenics-packages/+archive/ubuntu/fenics; compare version provided by `python3 -c "import dolfin;print(dolfin.__version__)`")
* OpenFOAM `2412`
* deal.II `9.5.1` (from https://launchpad.net/ubuntu/+source/deal.ii/9.5.1-2build3)

[^1]: Chen, Jun; Chourdakis, Gerasimos; Desai, Ishaan; Homs-Pons, Carme; Rodenberg, Benjamin; Schneider, David; Simonis, Frédéric; Uekermann, Benjamin; Davis, Kyle; Jaust, Alexander; Kelm, Mathis; Kotarsky, Niklas; Kschidock, Helena; Mishra, Durganshu; Mühlhäußer, Markus; Schrader, Timo Pierre; Schulte, Miriam; Seitz, Valentin; Signorelli, Joseph; van Zwieten, Gertjan; Vinnitchenko, Niklas; Vladimirova, Tina; Willeke, Leonard; Zonta, Elia. *preCICE Distribution Version v2404.0*. DaRUS, 2024, V1. https://doi.org/10.18419/darus-4167.
[^2]: Rodenberg, Benjamin. *Flexible and robust time stepping for partitioned multiphysics*. Technical University of Munich, 2025.
