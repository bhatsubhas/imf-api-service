from flask_restful import Resource

class Health(Resource):
    def get(self):
        return {
            "message": "Service status is healthy"
        }, 200