USER=jimho

generate_dockerfiles:
	./generate_dockerfile.py $$(cat versions | tr '\n' ' ')
