# Plotting

This folder `plotting` contains the LaTeX sources and auxiliary scripts to create figures and tables.

## Structure

The subfolders refer to the test cases provided in Section 4 Results and follow the naming convention of the three test cases at the root level of this repository:

* `plotting/oscillator-overlap` corresponds to *Section 4.1 Partitioned oscillator*
* `plotting/partitioned-heat-conduction` corresponds to *Section 4.2 Partitioned heat conduction*
* `plotting/perpendicular-flap` corresponds to *Section 4.3 Perpendicular flap*

Each of these folders contains subfolders names `FigX` or `TabX` for the respective figures and tables from the sections. These folders contain:

* `*.tex` files with the LaTeX sources
* `data` folder with the results produced by the respective test case. For convenience the data is already provided here. If you want to compute this data on your own, please refer to the `README.md` in the root folder of this.
* A `Makefile` to create a PDF file with the respective figure.

## Prerequisites

For creating the figures and tables you need a working LaTeX installation and Python with the packages `scipy`, `pandas`, `jinja2`, and `matplotlib`.

### Use docker

The `Dockerfile` in this folder allows you to create a docker container with all the required dependencies. Please install Docker on your operating system by following the instructions given on https://docs.docker.com/engine/install/.

On Ubuntu you can then build the docker container by running the following command from this folder:

```sh
docker build -t waveform-plotting .
```

You can also use a name of your choice instead of `waveform-plotting`.

### Use your own system

You need a working LaTeX installation and some Python packages on your system. On Ubuntu you can install all required packages by running

```sh
apt install texlive-full
apt install python3 python3-pip
```

Please install additional Python packages either via your package manager by running

```sh
apt install python3-pygments python3-pandas python3-scipy python3-jinja2
```

or you can also use virtual environment by first installing `python3-venv` and then installing the packages given in the `requirements.txt` from this folder:

```sh
apt install python3-venv
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