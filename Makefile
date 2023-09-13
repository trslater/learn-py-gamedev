.PHONY: install dev

dist:
	pyinstaller scripts/run.py \
        --onefile \
        --windowed \
        --name game

install:
	pip install -e .

dev:
	pip install -e '.[dev]'
