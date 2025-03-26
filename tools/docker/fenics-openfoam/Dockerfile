FROM precice/precice:3.2.0rc1

USER root

SHELL ["/bin/bash", "-c"]

# Install tooling
RUN apt-get -qq update && \
    apt-get -yy upgrade && \
    apt-get -qq install --no-install-recommends wget software-properties-common
    # rm -rf /var/lib/apt/lists/*

# Install OpenFOAM & add to bashrc
RUN wget -q -O - https://dl.openfoam.com/add-debian-repo.sh | bash && \
    apt-get -qq update && \
    apt-get -qq install openfoam2412-dev && \
    rm -rf /var/lib/apt/lists/* && \
    echo '. /usr/lib/openfoam/openfoam2412/etc/bashrc' >> /root/.bashrc && \
    echo '. /usr/lib/openfoam/openfoam2412/etc/bashrc' >> /home/precice/.bashrc

# Install FEniCS
RUN add-apt-repository -y ppa:fenics-packages/fenics && \
    apt-get -qq update && \
    apt-get -qq install --no-install-recommends fenics && \
    rm -rf /var/lib/apt/lists/*
  
# Install OpenFOAM adapter (Overwrite FOAM_USER_LIBBIN to install globally)
RUN wget https://github.com/precice/openfoam-adapter/releases/download/v1.3.1/openfoam-adapter-v1.3.1-OpenFOAMv1812-v2406-newer.tar.gz && \
    tar -xzf openfoam-adapter-v1.3.1-OpenFOAMv1812-v2406-newer.tar.gz && \
    cd openefoam-adapter-v1.3.1-master && \
    . /root/.bashrc && \
    export FOAM_USER_LIBBIN=$FOAM_LIBBIN && \
    ./Allwmake

