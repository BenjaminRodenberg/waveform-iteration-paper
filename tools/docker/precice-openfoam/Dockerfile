# Based on https://github.com/precice/precice/blob/625092d2c2f23f021708e8d74228d523742d1e1f/tools/releasing/packaging/docker/release.dockerfile

# Use OpenFOAM docker container as basis.
FROM opencfd/openfoam-run:2412
# Remove OpenFOAM PPA
RUN rm /etc/apt/sources.list.d/openfoam.list
# Add the precice user
RUN useradd -m -s /bin/bash precice
# Fix the installation of tzdata for Ubuntu
ARG TIMEZONE=Europe/Berlin
RUN export TZ=$TIMEZONE && echo $TZ > /etc/timezone && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    apt-get -yy update && apt-get -yy install wget tzdata lsb-release && rm -rf /var/lib/apt/lists/*
# The version to fetch the package for: X.Y.Z
ARG version=3.2.0
RUN echo "$version" | grep "[0-9]\+\.[0-9]\+\.[0-9]\+" > /dev/null # The version must follow the format X.Y.Z
RUN wget -q -O libprecice.deb https://github.com/precice/precice/releases/download/v${version}/libprecice`echo ${version} | sed 's/\([0-9]\+\)\.\([0-9]\+\.[0-9]\+\)/\1_\1.\2/'`_$(lsb_release -sc).deb && \
    apt-get update && apt-get -yy install ./libprecice.deb && \
    rm libprecice.deb && rm -rf /var/lib/apt/lists/*
# Make sure the installation is functional
RUN precice-tools version
