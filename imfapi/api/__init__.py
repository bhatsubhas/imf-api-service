from flask import Blueprint

api = Blueprint("api", __name__)

from . import health, exchange_rate, error