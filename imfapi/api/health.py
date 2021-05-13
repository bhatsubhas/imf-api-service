from . import api


@api.route("/health")
def get_health():
    return {"message": "Service status is healthy"}, 200
