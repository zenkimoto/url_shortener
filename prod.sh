#!/bin/sh

source venv/bin/activate

export FLASK_ENV=production
export FLASK_APP=src/main.py
flask run --host=0.0.0.0