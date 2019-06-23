"""Use this file for importing and creating instances for all of the extensions.

This file contains the instances of all of the extensions required for this Flask
application.
"""
from flask_restplus import Api

from app.routes.test_route import api as test_ns

api = Api()
api.add_namespace(test_ns)
