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

[^1]: Chen, Jun; Chourdakis, Gerasimos; Desai, Ishaan; Homs-Pons, Carme; Rodenberg, Benjamin; Schneider, David; Simonis, Frédéric; Uekermann, Benjamin; Davis, Kyle; Jaust, Alexander; Kelm, Mathis; Kotarsky, Niklas; Kschidock, Helena; Mishra, Durganshu; Mühlhäußer, Markus; Schrader, Timo Pierre; Schulte, Miriam; Seitz, Valentin; Signorelli, Joseph; van Zwieten, Gertjan; Vinnitchenko, Niklas; Vladimirova, Tina; Willeke, Leonard; Zonta, Elia. *preCICE Distribution Version v2404.0*. DaRUS, 2024, V1. https://doi.org/10.18419/darus-4167.
[^2]: Rodenberg, Benjamin. *Flexible and robust time stepping for partitioned multiphysics*. Technical University of Munich, 2025. Unpublished manuscript. Available at: https://doi.org/**TODO**.
