from flask import Flask
from api.imf.routes import imf_api
from api.task.routes import task_api
from api.handlers import (
    handle_not_found, handle_unsupported_media_type, handle_exception
)


def create_app():
    app = Flask(__name__)

    app.register_blueprint(imf_api)
    app.register_blueprint(task_api)

    app.register_error_handler(404, handle_not_found)
    app.register_error_handler(415, handle_unsupported_media_type)
    app.register_error_handler(Exception, handle_exception)

    @app.get("/health")
    def get_health():
        return {"message": "Service status is healthy"}, 200

    return app
