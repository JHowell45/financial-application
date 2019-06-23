"""Use this file for creating a test endpoint for checking the Flask application."""
from flask_restplus import Namespace, Resource

api = Namespace(
    "test",
    description=(
        "test endpoint for checking the application works and can be connected to."
    ),
)


@api.route("/")
class TestEndpointRoute(Resource):
    def get(self):
        return {"test": "all good!"}
