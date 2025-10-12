# Experiments

This folder `experiments` contains the scenarios and all required data and helper scripts needed to run the experiments.

## Overview

The subfolders of this folder refer to the test cases provided in Section 4 Results and follow the naming convention of the three test cases at the root level of this repository:

* `experiments/oscillator-overlap` corresponds to *Section 4.1 Partitioned oscillator*
* `experiments/partitioned-heat-conduction` corresponds to *Section 4.2 Partitioned heat conduction*
* `experiments/perpendicular-flap` corresponds to *Section 4.3 Perpendicular flap*

In the following sections of this document provide installation instructions for the necessary dependencies for running the cases and instructions on how to run the individual cases. The cases closely follow the tutorial cases from the preCICE distribution version v2404.0 [^Chen2024]. Please refer to the tutorial descriptions on [the preCICE website](https://precice.org/tutorials.html) or to the `README.md` files of the respective cases under [github.com/precice/tutorials](github.com/precice/tutorials) for details on the setups ([v2024.04](https://github.com/precice/tutorials/tree/v202404.0)).

## Dependencies & installation steps

You can start from a recent Linux-based system (Ubuntu 24.04 is recommended). Alternatively, the preCICE distribution version v2404.0 [^Chen2024] should provide a good basis for running the experiments provided in this repository.

In contrast to the preCICE distribution version v2404.0 a more recent version of preCICE and of some adapters will be required and have to be installed. The experiments are known to run as expected on a system with the following specification:

### preCICE components

* preCICE [`3.2.0`](https://github.com/precice/precice/releases/tag/v3.2.0)
* pyprecice [`3.2.1`](https://github.com/precice/python-bindings/releases/tag/v3.2.1) (automatically installed via `requirements.txt` of the respective case)
* FEniCS adapter [`2.2.0`](https://github.com/precice/fenics-adapter/releases/tag/v2.2.0) (automatically installed via `requirements.txt` of the respective case)
* OpenFOAM adapter [`1.3.1`](https://github.com/precice/openfoam-adapter/releases/tag/v1.3.1)

### OS and other dependencies

* Ubuntu (recommended `24.04`) or other Linux-based system
* The Python package [prepesthel](https://pypi.org/project/prepesthel/) for automation of preCICE runs (automatically installed via `requirements.txt` of the respective case)
* Additional python packages (automatically installed via `requirements.txt` of the respective case)
* FEniCS `2019.2.0.64.dev0` (installed from FEniCS PPA https://launchpad.net/~fenics-packages/+archive/ubuntu/fenics; compare version provided by `python3 -c "import dolfin;print(dolfin.__version__)"` or run `fenics-version`)
* OpenFOAM `2412` from OpenCFD / ESI (openfoam.com)

### Installing the required dependencies

The following steps will install the required dependencies on Ubuntu 24.04:

1. **preCICE**: Download the Debian package (`.deb`) of preCICE 3.2.0 from [here](https://github.com/precice/precice/releases/tag/v3.2.0) and install it on your system by running the command

   ```sh
   wget https://github.com/precice/precice/releases/download/v3.2.0/libprecice3_3.2.0_noble.deb
   sudo apt install -y libprecice3_3.2.0_noble.deb
   ```

   Note: The code name `noble` refers to Ubuntu 24.04, see [here](https://documentation.ubuntu.com/project/release-team/list-of-releases/). If you are using a different Ubuntu version, please replace `noble` with the respective code name.

2. **FEniCS**: Enter the following commands:

   ```sh
   sudo apt install -y software-properties-common
   sudo add-apt-repository -y ppa:fenics-packages/fenics
   sudo apt update
   sudo apt install -y fenics
   ```

   These installation instructions similar to the instructions from [here](https://fenicsproject.org/download/archive/).

3. **OpenFOAM 2414**: Enter the following commands:

   ```sh
   curl -s https://dl.openfoam.com/add-debian-repo.sh | sudo bash
   sudo apt update
   sudo apt install -y openfoam2412-default
   ```

   These installation instructions are similar to the instructions from [here](https://develop.openfoam.com/Development/openfoam/-/wikis/precompiled/debian). After that, you also need to source the OpenFOAM bashrc file:

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

5. **pyprecice, the FEniCS adapter, and other Python dependencies**: These dependencies will be fetched automatically from PyPI and installed into an individual virtual environment for each case for setting up the virtual environment, please execute the following commands:

   ```sh
   cd oscillator-overlap
   ./make-venv.sh
   ```

   The command above will create a virtual environment with all the required Python dependencies in the folder `.venv` in `oscillator-overlap`. You can easily get a list of the installed Python packages by running `.venv/bin/pip freeze` from `oscillator-overlap` and you should see `pyprecice` and `prepesthel` in this list. If you want to run one of the other cases please replace `oscillator-overlap` with `partitioned-heat-conduction` or `perpendicular-flap` above.

## Running the test cases

Each case is represented by a subfolder `oscillator-overlap`, `partitioned-heat-conduction`, and `perpendicular-flap`. They are forked from the preCICE tutorials from [github.com/precice/tutorials](github.com/precice/tutorials) and follow their basic structure. Additionally, they contain some helper scripts needed for setting up the runtime environment, running the experiments, and postprocessing data for plotting:

* The script `make-venv.sh` allows to create a virtual environment needed for running the experiments (see above for usage).
* A helper script `run_experiments.sh` that will automatically run all experiments required for each study (convergence study, comparison of iteration numbers etc.). It is recommended to navigate to the respective folder and run this script. This should automatically execute all experiments.
* A folder `configs` with `.csv` files defining configurations (e.g., time window sizes or time step sizes) for individual experiments.
* A folder `results`. After running the experiments this folder will contain all the relevant data for creation of the plots.
* Python scripts `doConvergenceStudy.py`, respectively `doConvergenceStudyMonolithic.py` required for automation of experiment runs via the Python package [prepesthel](https://pypi.org/project/prepesthel/).
* In contrast to the original preCICE tutorials there is no `precice-config.xml` but a `precice-config.xml.jinja2` Jinja2 template. This template will be processed by the Jinja2 engine to create preCICE configuration files for the respective experiments.

### Example: Run experiments from Section 4.1

If you want to run, for example, all experiments from *Section 4.1 Partitioned oscillator* please navigate to the folder `oscillator-overlap` and run the experiments by executing the helper script (this will take a while):

```
cd oscillator-overlap
./run_experiments.sh
```

For other experiments, simply replace `oscillator-overlap` with `partitioned-heat-conduction` or `perpendicular-flap`.

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

You can copy this data to the respective location in the `plotting` folder at the root of this repository or use precomputed data already present at this location.

[^Chen2024]: Chen, Jun; Chourdakis, Gerasimos; Desai, Ishaan; Homs-Pons, Carme; Rodenberg, Benjamin; Schneider, David; Simonis, Frédéric; Uekermann, Benjamin; Davis, Kyle; Jaust, Alexander; Kelm, Mathis; Kotarsky, Niklas; Kschidock, Helena; Mishra, Durganshu; Mühlhäußer, Markus; Schrader, Timo Pierre; Schulte, Miriam; Seitz, Valentin; Signorelli, Joseph; van Zwieten, Gertjan; Vinnitchenko, Niklas; Vladimirova, Tina; Willeke, Leonard; Zonta, Elia. *preCICE Distribution Version v2404.0*. DaRUS, 2024, V1. https://doi.org/10.18419/darus-4167.
