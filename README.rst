Pick-it docs
============

Build html on Docker
--------------------
A Dockerfile is included to build the html with the ReadTheDocs Theme locally.

Build the image: `docker build --tag=pickit-docs .`

Build the documentation:

.. code-block:: bash
    docker run --rm -v ~/pickit-docs:/docs -t pickit-docs:latest bash -c "\
    mkdir -p /docs/_build/html && \
    cd /docs/docs && \
    mkdir _build && \sphinx-build -b html . ../_build/html"

The errors of the build process are printed on screen and the build is available in `_build/html`.