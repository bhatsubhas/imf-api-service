#!/usr/bin/env bash

source ./venv/bin/activate
gunicorn imfapi.app:app
