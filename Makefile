.PHONY: dist install dev clean

dist:
	pyinstaller scripts/run.py \
		--add-data "game.toml:." \
		--onefile \
		--windowed \
		--name game

install:
	pip install -e .

dev:
	pip install -e '.[dev]'

clean:
	rm -fr ./build
	rm -fr ./dist
	rm game.spec
