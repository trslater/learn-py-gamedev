# Python Game Dev

This repo is just for learning Python game dev using [Arcade](https://api.arcade.academy).

## Makefile

This project uses Make to automate lifecycle tasks. To see the underlying commands, just inspect the `Makefile`.

## Installation

To install the game for local play through your local Python install:

```
make install
```

## Usage

```
game
```

## Development

To install the game with dev dependencies:

```
make dev
```

## Distribution

To build an executable for distribution:

```
make
```

**Note**: PyInstaller (the package used to build the executable) will automatically build an executable for the current platform. To build for multiple environments, you must run make on each type of machine you want to distribute to (e.g., Mac, PC).

## Requirements

I have opted to *not* include main dependencies in the `requirements-dev.txt` file to avoid discrepancies between requirements.
