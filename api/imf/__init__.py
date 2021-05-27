from flask import Blueprint

imf_api = Blueprint("imf", __name__)

from . import exchange_rate
