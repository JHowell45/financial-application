"""Use this file for creating a test endpoint for checking the Flask application."""
from flask_restplus import Namespace, Resource

api = Namespace(
    "tests",
    description=(
        "test endpoint for checking the application works and can be connected to."
    ),
)


@api.route("/1")
class Test1(Resource):
    def get(self):
        return {"test": "all good!"}


@api.route("/2")
class Test2(Resource):
    def get(self):
        return {"test": 3}
