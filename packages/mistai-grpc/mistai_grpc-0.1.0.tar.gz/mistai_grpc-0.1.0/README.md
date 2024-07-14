# How-to Guide

## Project structure

```
base-folder
setup.py
.env (not included)
Makefile
requirements.txt
README.md
|-- libname (dir)
    |-- __init__.py
    |-- *.py
```

## .env file

`Note:` Please rename the .env-template to .env and add credentials

## How to build

```shell
# Build
make build
```

## How to deploy to PyPi

```shell
# Build
make publish
```
