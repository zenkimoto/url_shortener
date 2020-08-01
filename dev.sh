#!/bin/sh

source venv/bin/activate

export FLASK_ENV=development
export FLASK_APP=src/main.py
flask run