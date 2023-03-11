.PHONY: all clean build deploy

all: clean build deploy

clean:
	rm -rf dist/

build:
	pip install -U build
	python3 -m build

deploy:
	pip install -U twine
	python3 -m twine upload dist/*
