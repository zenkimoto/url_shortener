#!/bin/sh

export FLASK_ENV=production
export FLASK_APP=src/main.py
flask run --host=0.0.0.0