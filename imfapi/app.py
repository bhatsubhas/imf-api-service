from flask import Flask, Blueprint
from flask.json import jsonify
from flask_restful import Api
from werkzeug.exceptions import HTTPException
from imfapi.resources.health import Health
from imfapi.resources.exchange_rate import ExchangeRateFile

api_bp = Blueprint('api', __name__)
api = Api(api_bp, catch_all_404s=True)
app = Flask(__name__)
app.register_blueprint(api_bp)


@api_bp.errorhandler(Exception)
def handle_exception(e):
    api_bp.logger.error(e)
    if isinstance(e, HTTPException):
        return e

    return {
        "Error": "Something went wrong internally"
    }, 500


api.add_resource(Health, '/health')
api.add_resource(ExchangeRateFile, '/exchangeRateFile')
