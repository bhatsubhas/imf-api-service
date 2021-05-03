#!/usr/bin/env bash

source venv/bin/activate

export FLASK_APP=imfapi.app
export FLASK_ENV=development
flask run
