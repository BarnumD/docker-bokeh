#!/bin/bash
docker build -t jimho/bokeh:$1 -f Dockerfile_$1 . && docker push jimho/bokeh:$1
