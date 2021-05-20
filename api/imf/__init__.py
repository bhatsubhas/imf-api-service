from flask import Blueprint

imf_api = Blueprint("imf", __name__)

from . import health, exchange_rate, error
