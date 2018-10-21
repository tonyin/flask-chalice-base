# flask-chalice-base
Base for python3, flask, chalice

## Requirements

* python3.6
* aws credentials

## Installation

1. `python3 -m venv venv`
2. `. venv/bin/activate`
3. `pip install chalice`

To start a new project, `chalice new-project flask-chalice-base`

## Project Structure

Chalice installs into a new directory inside the root directory holding the virtual environment.

## Develop

1. `. venv/bin/activate`
2. `cd flask-chalice-base`
3. `chalice local`

## Deployment

1. dev: `chalice deploy --stage dev`
2. prod: `chalice deploy --stage prod`
