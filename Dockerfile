FROM readthedocs/build:latest

# Set the working directory
WORKDIR /docs

# Install sphinx and RTD Theme
RUN pip3 install sphinx sphinx_rtd_theme
