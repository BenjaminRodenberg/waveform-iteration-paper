# Replication Data for: A Waveform Iteration Implementation for Black-box Multi-rate Higher-order Coupling

This repository contains all the data needed for performing the experiments and producing the plots from "A waveform iteration implementation for black-box multi-rate higher-order coupling" [^RodenbergUekermann2025].

It is a fork of https://github.com/BenjaminRodenberg/test-cases-dissertation with test cases from Benjamin Rodenberg's dissertation "Flexible and robust time stepping for partitioned multiphysics" [^Rodenberg2025]. The test cases are modified versions of the tutorials from https://github.com/precice/tutorials/releases/tag/v202404.0 [^Chen2024].

This repository contains the following folders:

* `experiments`: The definition of the setups and scripts to execute the experiments. The structure of this folder closely follows https://github.com/precice/tutorials/releases/tag/v202404.0.
* `plotting`: Scripts for creating plots from the data produced by the experiments. This folder also contains pre-computed data obtained by running the scenarios from `experiments`
* `tools`: Miscellaneous files for tooling and automation
* `.github/workflows`: Definition of pipelines that allow to perform the experiments using [GitHub Actions](https://github.com/features/actions). You can fork this repository to run the experiments and create the plots with github actions. Alternatively, you can also find the artifacts created by the GitHub Actions pipeline on the branch [`gh-pages`](https://github.com/BenjaminRodenberg/test-cases-dissertation/tree/gh-pages).

The folders `experiments` and `plotting` contain subfolders corresponding to the following subsections of the results section of[^Rodenberg2025]:

* `oscillator-overlap`: 4.1 Oscillator problem 
* `partitioned-heat-conduction`: 4.2 Partitioned heat conduction
* `perpendicular-flap`: 4.3 Perpendicular flap

If you want to run the experiments from the paper, please refer to `experiments/README.md` for further instructions. If you want to create the plots from given results, please refer to `plotting/README.md`.

[^RodenbergUekermann2025]: Rodenberg, Benjamin; Uekermann, Benjamin. *A waveform iteration implementation for black-box multi-rate higher-order coupling*. [Manuscript in preparation]
[^Chen2024]: Chen, Jun; Chourdakis, Gerasimos; Desai, Ishaan; Homs-Pons, Carme; Rodenberg, Benjamin; Schneider, David; Simonis, Frédéric; Uekermann, Benjamin; Davis, Kyle; Jaust, Alexander; Kelm, Mathis; Kotarsky, Niklas; Kschidock, Helena; Mishra, Durganshu; Mühlhäußer, Markus; Schrader, Timo Pierre; Schulte, Miriam; Seitz, Valentin; Signorelli, Joseph; van Zwieten, Gertjan; Vinnitchenko, Niklas; Vladimirova, Tina; Willeke, Leonard; Zonta, Elia. *preCICE Distribution Version v2404.0*. DaRUS, 2024, V1. https://doi.org/10.18419/darus-4167.
[^Rodenberg2025]: Rodenberg, Benjamin. *Flexible and robust time stepping for partitioned multiphysics*. Technical University of Munich, 2025. https://nbn-resolving.org/urn:nbn:de:bvb:91-diss-20250424-1763172-0-4