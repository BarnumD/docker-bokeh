#!/usr/bin/env python
from __future__ import division, print_function

from toolz.curried import (
    map,
    juxt,
    compose,
)


def get_dockerfile(version):
    return (
        "FROM ubuntu:14.04\n"
        "\n"
        "RUN useradd --create-home --home-dir /opt/bokeh --shell /bin/bash bokeh\n"
        "\n"
        "RUN apt-get update && apt-get install --assume-yes \\\n"
        "    python \\\n"
        "    python-pip \\\n"
        "    npm \\\n"
        "    nodejs-legacy \\\n"
        "    gcc \\\n"
        "    gfortran \\\n"
        "    libblas-dev \\\n"
        "    liblapack-dev \\\n"
        "    cython \\\n"
        "    build-essential \\\n"
        "    python-dev\n"
        "\n"
        "ADD https://pypi.python.org/packages/source/b/bokeh/bokeh-{version}.tar.gz /tmp/bokeh-{version}.tar.gz\n"
        "RUN tar -xvf /tmp/bokeh-{version}.tar.gz && mv bokeh-{version} /opt/bokeh/bokeh\n"
        "\n"
        "WORKDIR /opt/bokeh/bokeh\n"
        "\n"
        "RUN pip install -e .\n"
        "RUN python setup.py install\n"
        "\n"
        "USER bokeh\n"
        "ENV HOME /opt/bokeh\n"
        "ENV USER bokeh\n"
        "EXPOSE 5000\n"
        "\n"
        "ENTRYPOINT [ \"bokeh-server\" ]\n"
        "CMD [ \"--ip=0.0.0.0\", \"--port=5000\" ]\n"
    ).format(version=version)


def write_file((filename, data)):
    print("Write '{}' .. ".format(filename), end="")
    with open(filename, 'w') as f:
        f.write(data)
    print("OK")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generates bokeh Dockerfile for given version")
    parser.add_argument("version", type=str, nargs="*")
    args = parser.parse_args()

    list(map(
        compose(
            write_file,
            juxt([
                "Dockerfile_{}".format,
                get_dockerfile
            ])
        ),
        args.version
    ))
