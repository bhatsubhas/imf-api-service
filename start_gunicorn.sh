#!/usr/bin/env bash

source ./venv/bin/activate
gunicorn api.app:app
