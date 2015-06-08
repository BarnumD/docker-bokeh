#!/bin/bash
echo "$(cat Dockerfile | grep bokeh)"
docker build -t jimho/bokeh:latest . && docker push jimho/bokeh:latest
