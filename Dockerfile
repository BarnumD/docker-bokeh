FROM phusion/baseimage

RUN useradd --create-home --home-dir /opt/bokeh --shell /bin/bash bokeh

RUN apt-get update && apt-get install --assume-yes \
    python \
    python-pip \
    npm \
    nodejs-legacy \
    gcc \
    gfortran \
    libblas-dev \
    liblapack-dev \
    cython \
    build-essential \
    python-dev

ADD https://pypi.python.org/packages/source/b/bokeh/bokeh-0.9.0.tar.gz /tmp/bokeh-0.9.0.tar.gz
RUN tar -xvf /tmp/bokeh-0.9.0.tar.gz && mv bokeh-0.9.0 /opt/bokeh/bokeh

WORKDIR /opt/bokeh/bokeh

RUN pip install -e .
RUN python setup.py install

USER bokeh
ENV HOME /opt/bokeh
ENV USER bokeh
EXPOSE 5006

mkdir -p /etc/service/bokeh; \
echo "bokeh-server --ip=0.0.0.0", "--port=5006" > /etc/service/bokeh/run

CMD ["/sbin/my_init"]
