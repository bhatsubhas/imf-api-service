from flask import Flask
from .imf import imf_api
from .task import task_api


app = Flask(__name__)
app.register_blueprint(imf_api, url_prefix="/api/v1/exchangeRate")
app.register_blueprint(task_api, url_prefix="/api/v1/task")
