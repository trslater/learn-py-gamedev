from functools import cache
from pathlib import Path

import tomllib

ROOT_PATH = Path(__file__, "../..").resolve()


@cache
def config():
    with open(ROOT_PATH/"config.toml", "rb") as config_file:
        return tomllib.load(config_file)
