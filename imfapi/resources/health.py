from flask_restx import Resource


class Health(Resource):
    def get(self):
        return {"message": "Service status is healthy"}, 200
