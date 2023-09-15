.PHONY: dist install dev clean

dist:
	pyinstaller scripts/run.py \
		--add-data "src/config.toml:." \
		--add-data "assets:assets" \
		--onefile \
		--windowed \
		--name game

deploy:
	butler push dist trslater/test-project:osx-alpha

install:
	pip install -e .

dev:
	pip install -e '.[dev]'

clean:
	rm -fr ./build
	rm -fr ./dist
	rm game.spec
