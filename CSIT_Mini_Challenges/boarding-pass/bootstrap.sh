#!/bin/sh
FLASK_APP=./server/index.py
export FLASK_APP
pipenv run flask --debug run -h 0.0.0.0