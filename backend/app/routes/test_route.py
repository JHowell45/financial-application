"""

"""
from flask_restplus import Resource

from app.extensions import api


@api.route("/test")
class TestEndpointRoute(Resource):
    def get(self):
        return {"test": "all good!"}
