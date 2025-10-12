# Plotting

This folder `plotting` contains the LaTeX sources and auxiliary scripts to create figures and tables.

## Overview

The subfolders refer to the test cases provided in *Section 4* Results and follow the naming convention of the three test cases at the root level of this repository:

* `plotting/oscillator-overlap` corresponds to *Section 4.1 Partitioned oscillator*
* `plotting/partitioned-heat-conduction` corresponds to *Section 4.2 Partitioned heat conduction*
* `plotting/perpendicular-flap` corresponds to *Section 4.3 Perpendicular flap*

Additionally, there are the following files for automation of the plotting:

* A `Dockerfile` to setup the runtime environment in Docker (see below)
* A `requirements.txt` to define the Python dependencies needed for plotting
* A `Makefile` that allows to automatically perform preprocessing steps and create the plots for all cases

The subfolders corresponding to the test cases contain subfolders named `FigX` or `TabX` for the respective figures and tables from *Section 4 Results*. These folders contain:

* `*.tex` files with the LaTeX sources or (for more complex plots) `*.tex.jinja2` templates that will be filled with data using a Python script and Jinja2 to create a `*.tex` file in a preprocessing step.
* `data` folder with the results produced by the respective test case. For convenience the data is already provided here. If you want to compute this data on your own, please refer to the `experiments/README.md`.
* A `Makefile` to create PDF files with the respective figures or tables.

## Prerequisites

For creating the figures and tables you need a working LaTeX installation and Python with the packages `scipy`, `pandas`, `jinja2`, and `matplotlib`. It is recommended to use Ubuntu 24.04. But the workflow should be similar for other Ubuntu versions or Linux-based systems.

### Use docker

The `Dockerfile` in this folder allows you to create a docker container with all the required dependencies. Please install Docker on your operating system by following the instructions given on https://docs.docker.com/engine/install/.

You can then build the docker container by running the following command from this folder:

```sh
docker build -t waveform-plotting .
```

You can also use a name of your choice instead of `waveform-plotting`.

### Use your own system

You need a working LaTeX installation and some Python packages on your system. Please install all required packages by running

```sh
sudo apt install -y texlive-full
sudo apt install -y python3 python3-pip
```

Please install additional Python packages either via your package manager by running

```sh
sudo apt install -y python3-pygments python3-pandas python3-scipy python3-jinja2
```

alternatively, you can use a virtual environment. This will require installing `python3-venv` and then the packages given in the `requirements.txt` from this folder:

```sh
sudo apt install -y python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

This will create a virtual environment `.venv`. Please ensure that this virtual environment is active when trying to create the figures and table as described below

## Creating the figures and tables

If you installed the prerequesites as described above on your own system please run `make` from this folder to create all figures and tables. To create individual figures and tables, please navigate to the respective folder and run `make` there.

If you are using docker, instead of running `make` use the following command to run the `make` command in the docker container and write the output back to your file system:

```sh
docker run --rm -v "$PWD":/doc -w /doc siam-pdflatex make
```

This procedure also works for individual figures and tables if you run it from the respective folder.

### Example: Create Figure 11

If you, for example, only want to create Figure 11, please navigate to the respective folder and execute `make`:

```sh
cd oscillator-overlap/Fig11
make
```

This should create the file `main.pdf` with Figure 11 using the precomputed data from `plotting/oscillator-overlap/Fig11/data`.

If you want to start from scratch and use data that you computed on your own system, please delete the folder `plotting/oscillator-overlap/Fig11/data` and copy the data from `experiments/oscillator-overlap/results/Fig11/data` to the correct location (see `experiments/README.md` for instructions how to create this data):

```sh
rm -r oscillator-overlap/Fig11/data
cp -r ../experiments/oscillator-overlap/results/Fig11/data oscillator-overlap/Fig11/data
cd oscillator-overlap/Fig11
make
```

This should again result in a file `main.pdf` with Figure 11.
