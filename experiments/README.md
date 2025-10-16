# Experiments

This folder `experiments` contains the scenarios and all required data and helper scripts needed to run the experiments.

## Overview

The subfolders of this folder refer to the test cases provided in *Section 4 Results*:

* `experiments/oscillator-overlap` corresponds to *Section 4.1 Partitioned oscillator*
* `experiments/partitioned-heat-conduction` corresponds to *Section 4.2 Partitioned heat conduction*
* `experiments/perpendicular-flap` corresponds to *Section 4.3 Perpendicular flap*

The following sections of this README document provide installation instructions for necessary dependencies and instructions on how to run the cases. The cases closely follow the [tutorial cases from the preCICE distribution version v2404.0](https://github.com/precice/tutorials/tree/v202404.0) [^Chen2024]. Refer to the tutorial descriptions on [the preCICE website](https://precice.org/tutorials.html) for details on the setups.

## Dependencies & installation steps

You can start from a recent Linux-based system (Ubuntu 24.04 is recommended). The experiments are known to run on a system with the following specification:

### preCICE components

* preCICE [`3.3.0`](https://github.com/precice/precice/releases/tag/v3.3.0)
* pyprecice [`3.3.1`](https://github.com/precice/python-bindings/releases/tag/v3.3.1) (automatically installed via `requirements.txt` of the respective cases)
* FEniCS adapter [`2.2.0`](https://github.com/precice/fenics-adapter/releases/tag/v2.2.0) (automatically installed via `requirements.txt` of the respective cases)
* OpenFOAM adapter [`1.3.1`](https://github.com/precice/openfoam-adapter/releases/tag/v1.3.1)

### Other dependencies

* The Python package [prepesthel](https://pypi.org/project/prepesthel/) for automation of preCICE runs (automatically installed via `requirements.txt` of the respective cases)
* Additional python packages (automatically installed via `requirements.txt` of the respective cases)
* FEniCS `2019.2.0.64.dev0` (installed from FEniCS PPA https://launchpad.net/~fenics-packages/+archive/ubuntu/fenics; compare version provided by `python3 -c "import dolfin;print(dolfin.__version__)"` or run `fenics-version`)
* OpenFOAM `2412` from OpenCFD / ESI (openfoam.com)

### Installing the required dependencies

The following steps will install the required dependencies:

1. **preCICE**: Download the Debian package (`.deb`) of [preCICE v3.3.0](https://github.com/precice/precice/releases/tag/v3.3.0) and install it on your system by running the command

   ```sh
   wget https://github.com/precice/precice/releases/download/v3.3.0/libprecice3_3.3.0_noble.deb
   sudo apt install -y libprecice3_3.3.0_noble.deb
   ```

   Note: The code name `noble` refers to Ubuntu 24.04, see [Ubuntu docs](https://documentation.ubuntu.com/project/release-team/list-of-releases/). If you are using a different Ubuntu version, please replace `noble` with the respective code name.

2. **FEniCS**: Enter the following commands:

   ```sh
   sudo apt install -y software-properties-common
   sudo add-apt-repository -y ppa:fenics-packages/fenics
   sudo apt update
   sudo apt install -y fenics
   ```

   These installation instructions are similar to the instructions the [FEniCS docs](https://fenicsproject.org/download/archive/).

3. **OpenFOAM 2414**: Enter the following commands:

   ```sh
   curl -s https://dl.openfoam.com/add-debian-repo.sh | sudo bash
   sudo apt update
   sudo apt install -y openfoam2412-default
   ```

   These installation instructions are similar to the instructions from the [OpenFOAM docs](https://develop.openfoam.com/Development/openfoam/-/wikis/precompiled/debian). After that, you also need to source the OpenFOAM bashrc file:

   ```sh
   source /usr/lib/openfoam/openfoam2412/etc/bashrc
   ```

   You can also append this line to your `~/.bashrc` file by running

   ```sh
   echo "source /usr/lib/openfoam/openfoam2412/etc/bashrc" >> ~/.bashrc
   ```

4. **OpenFOAM adapter**: Enter the following commands:

    ```sh
    wget https://github.com/precice/openfoam-adapter/releases/download/v1.3.1/openfoam-adapter-v1.3.1-OpenFOAMv1812-v2406-newer.tar.gz
    tar -xzf openfoam-adapter-v1.3.1-OpenFOAMv1812-v2406-newer.tar.gz
    cd openefoam-adapter-v1.3.1-master
    ./Allwmake
    ```

5. **pyprecice, the FEniCS adapter, and other Python dependencies**: These dependencies are fetched automatically from PyPI and installed into an individual virtual environment for each case. For example:

   ```sh
   cd oscillator-overlap
   ./make-venv.sh
   ```

   The command above creates a virtual environment with all required Python dependencies in the folder `.venv` in `oscillator-overlap`. You can get a list of the installed Python packages by running `.venv/bin/pip freeze`.

## Running the test cases

The test cases are forked from the [preCICE tutorials](https://github.com/precice/tutorials) and follow their basic structure. Additionally, they contain helper scripts for setting up the runtime environment, running the experiments, and postprocessing data for plotting:

* `make-venv.sh` creates a virtual environment needed for running the experiments (see above).
* `run_experiments.sh` runs all experiments required for each study (convergence study, comparison of iteration numbers etc.). It is recommended to navigate to the respective folder and run this script.
* Folder `configs` with `.csv` files defines configurations (e.g., time window sizes or time step sizes) for individual experiments.
* Folder `results` will contain all relevant data for creation of the plots after running the experiments.
* Python scripts `doConvergenceStudy.py` and `doConvergenceStudyMonolithic.py` are indirectly called by `run_experiments.sh` and use the Python package [prepesthel](https://pypi.org/project/prepesthel/) to execute multiple preCICE experiments and create reports with their results.
* In contrast to the original preCICE tutorials, there is no `precice-config.xml`, but a `precice-config.xml.jinja2` Jinja2 template. This template is processed by the Jinja2 engine to create preCICE configuration files for the respective experiments.

### Example: Run experiments from Section 4.1

If you want to run, for example, all experiments from *Section 4.1 Partitioned oscillator* please navigate to the folder `oscillator-overlap` and run the experiments by executing the helper script (this will take a while):

```
cd oscillator-overlap
./run_experiments.sh
```

After running the experiments, you will find all data in the `results` folder. For `oscillator-overlap` this looks as follows:

```
results/
├── Fig10
│   └── data
│       ├── piecewise_linear
│       │   ├── 0.0125_0.0025_0.000125
│       │   │   ├── precice-Mass-Left-iterations.log
│       │   │   ├── precice-Mass-Right-convergence.log
│       │   │   └── precice-Mass-Right-iterations.log
│       │   :
│       │   └── 0.2_0.04_0.002
│       │       ├── precice-Mass-Left-iterations.log
│       │       ├── precice-Mass-Right-convergence.log
│       │       └── precice-Mass-Right-iterations.log
│       ├── piecewise_linear.csv
│       ├── third_degree_b-spline
│       │   └── ...
│       └── third_degree_b-spline.csv
├── Fig11
│   └── data
│       ├── contour_data
│       │   ├── 0.00125_0.0003125_0.00015625
│       │   │   ├── precice-Mass-Left-iterations.log
│       │   │   ├── precice-Mass-Right-convergence.log
│       │   │   └── precice-Mass-Right-iterations.log
│       |   :
│       │   └── 0.2_0.05_9.765625e-05
│       │       ├── precice-Mass-Left-iterations.log
│       │       ├── precice-Mass-Right-convergence.log
│       │       └── precice-Mass-Right-iterations.log
│       └── contour_data.csv
└── Tab1
    └── data
        ├── FP
        │   └── ...
        ├── FP.csv
        ├── QN
        │   └── ...
        ├── QN.csv
        ├── rQN
        │   └── ...
        └── rQN.csv
```

You can copy this data to the respective location in the `plotting` folder at the root of this repository or instead use the precomputed data already there.

[^Chen2024]: Chen, Jun; Chourdakis, Gerasimos; Desai, Ishaan; Homs-Pons, Carme; Rodenberg, Benjamin; Schneider, David; Simonis, Frédéric; Uekermann, Benjamin; Davis, Kyle; Jaust, Alexander; Kelm, Mathis; Kotarsky, Niklas; Kschidock, Helena; Mishra, Durganshu; Mühlhäußer, Markus; Schrader, Timo Pierre; Schulte, Miriam; Seitz, Valentin; Signorelli, Joseph; van Zwieten, Gertjan; Vinnitchenko, Niklas; Vladimirova, Tina; Willeke, Leonard; Zonta, Elia. *preCICE Distribution Version v2404.0*. DaRUS, 2024, V1. https://doi.org/10.18419/darus-4167.
