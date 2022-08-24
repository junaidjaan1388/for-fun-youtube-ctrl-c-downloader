run:
	./main.py

install-deps:
	pip install -r requirements.txt

pip-compile:
	pip-compile --generate-hashes --no-emit-index-url --no-header

black:
	black .
