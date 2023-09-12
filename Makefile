.PHONY: install dev

install:
	pip install -e .

dev:
	pip install -e '.[dev]'
