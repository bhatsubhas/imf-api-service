from werkzeug.exceptions import HTTPException
from flask import jsonify


def handle_not_found(e):
    return jsonify({
        "error": "Resource not found"
    }), 404


def handle_unsupported_media_type(e):
    return jsonify({
        "error": "Unsupported Media Type"
    }), 415


def handle_exception(e):  # pragma: no cover
    if isinstance(e, HTTPException):
        return e

    return jsonify({
        "error": "Something went wrong internally"
    }), 500
