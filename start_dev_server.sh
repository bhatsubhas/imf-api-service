#!/usr/bin/env bash

source venv/bin/activate

export FLASK_APP=api.app
export FLASK_ENV=development
flask run
