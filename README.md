Run
----
docker run --net="host" jimho/bokeh:0.8.2

Build
-----
docker build -t bokeh:0.8.2 -f Dockerfile_0.8.2 .

Run your build
--------------
docker run --net="host" bokeh:0.8.2

Debug your build
----------------
docker run --net="host" -it bokeh:0.8.2 bash
