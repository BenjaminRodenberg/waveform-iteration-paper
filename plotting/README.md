# Plotting

This folder `plotting` contains the LaTeX sources and auxiliary scripts to create figures and tables.

## Overview

The subfolders refer to the test cases provided in *Section 4 Results*:

* `plotting/oscillator-overlap` corresponds to *Section 4.1 Partitioned oscillator*
* `plotting/partitioned-heat-conduction` corresponds to *Section 4.2 Partitioned heat conduction*
* `plotting/perpendicular-flap` corresponds to *Section 4.3 Perpendicular flap*

Additionally, there are the following files for automation of the plotting:

* `Dockerfile` to setup the runtime environment in Docker (see below)
* `requirements.txt` to define the Python dependencies needed for plotting
* `Makefile` to automatically perform preprocessing steps and create the plots for all cases

The subfolders corresponding to the test cases contain subfolders named `FigX` or `TabX` for the respective figures and tables from *Section 4 Results*. These folders contain:

* `*.tex` files with the LaTeX sources or (for more complex plots) `*.tex.jinja2` templates that will be filled with data using a Python script and Jinja2 to create a `*.tex` file in a preprocessing step.
* `data` folder with the results produced by the respective test case. For convenience, the data is already provided. If you want to compute the data on your own, please refer to `experiments/README.md`.
* `Makefile` to create PDF files with the respective figures or tables.

## Prerequisites

For creating the figures and tables you need a working LaTeX installation and Python with the packages `scipy`, `pandas`, `jinja2`, and `matplotlib`. It is recommended to use Ubuntu 24.04.

### Using docker

The `Dockerfile` allows creating a container with all required dependencies. [Install Docker on your system](https://docs.docker.com/engine/install/).

You can then build the Docker container:

```sh
docker build -t waveform-plotting .
```

### Use your own system

Install LaTex and Python:

```sh
sudo apt install -y texlive-full
sudo apt install -y python3 python3-pip
```

Install additional Python packages either via your package manager:

```sh
sudo apt install -y python3-pygments python3-pandas python3-scipy python3-jinja2
```

Or using a virtual environment. This requires installing `python3-venv` and then the packages given in the `requirements.txt`:

```sh
sudo apt install -y python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

This creates a virtual environment `.venv`. Activate with `source .venv/bin/activate`.

## Creating the figures and tables

If you installed the prerequesites on your own system, run `make` to create all figures and tables. To directly create individual figures and tables, navigate to the respective folder and run `make` there.

If you are using Docker, run `make` in the container and directly write output back to your system:

```sh
docker run --rm -v "$PWD":/doc -w /doc waveform-plotting make
```

This procedure also works for individual figures and tables if you run it from the respective folder.

### Example: Create Figure 11

If you only want to create Figure 11, navigate to the respective folder and execute `make`:

```sh
cd oscillator-overlap/Fig11
make
```

This creates the file `main.pdf` with Figure 11 using the precomputed data from `plotting/oscillator-overlap/Fig11/data`.
