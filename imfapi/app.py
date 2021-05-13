from flask import Flask
from .api import api as api_blueprint


app = Flask(__name__)
app.register_blueprint(api_blueprint, url_prefix="/api/v1/exchangeRate")
