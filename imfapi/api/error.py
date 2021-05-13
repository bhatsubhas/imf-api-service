from werkzeug.exceptions import HTTPException
from . import api


@api.app_errorhandler(404)
def handle_not_found_error(e):
    return {"Error": "Resource not found"}, 404


@api.app_errorhandler(Exception)
def handle_exception(e):  # pragma: no cover
    if isinstance(e, HTTPException):
        return e
    return {"Error": "Something went wrong internally"}, 500
