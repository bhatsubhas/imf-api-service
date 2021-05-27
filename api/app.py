from werkzeug.exceptions import HTTPException
from flask import Flask
from .imf import imf_api
from .task import task_api


app = Flask(__name__)
app.register_blueprint(imf_api, url_prefix="/api/v1/exchangeRate")
app.register_blueprint(task_api, url_prefix="/api/v1/task")


@app.errorhandler(404)
def handle_not_found_error(e):
    return {"Error": "Resource not found"}, 404


@app.errorhandler(Exception)
def handle_exception(e):  # pragma: no cover
    if isinstance(e, HTTPException):
        return e
    return {"Error": "Something went wrong internally"}, 500


@app.get("/health")
def get_health():
    return {"message": "Service status is healthy"}, 200
