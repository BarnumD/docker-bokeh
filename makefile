USER=jimho


generate_dockerfiles:
	./generate_dockerfile.py $$(cat versions | tr '\n' ' ')

try_build_and_push_all:
	cat versions | xargs -I{} bash -c 'function build_push { echo "build_push($$1)" && docker build -t ${USER}/bokeh-$$1 . && docker push ${USER}/bokeh-$$1;}; build_push {} || echo "FAILED"'
