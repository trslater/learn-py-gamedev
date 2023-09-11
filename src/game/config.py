from functools import cache

import tomllib

@cache
def config():
    with open("game.toml", "rb") as config_file:
        return tomllib.load(config_file)
