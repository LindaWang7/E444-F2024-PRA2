#!/bin/sh
. venv/bin/activate  # Use . instead of source for sh
export FLASK_APP=hello.py  # Set the correct Flask app
exec flask run --host=0.0.0.0 --port=5000
