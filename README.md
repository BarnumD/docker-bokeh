Run
----
docker run -p 5000:5000 -t jimho/bokeh:0.8.2

Build
-----
docker build -t bokeh:0.8.2 -f Dockerfile_0.8.2 .

Run your build
--------------
docker run -p 5000:5000 -t bokeh:0.8.2

Debug your build
----------------
docker run -p 5000:5000 -it bokeh:0.8.2 bash
