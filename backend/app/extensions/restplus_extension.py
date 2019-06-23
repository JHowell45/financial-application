"""Use this file for instancing the Flask Rest plus application and add routes."""
from flask_restplus import Api

from app.routes.test_route import api as test_ns

api = Api()
api.add_namespace(test_ns)
