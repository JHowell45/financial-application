"""Use this file for instancing the Flask Rest plus application and add routes."""
from flask_restx import Api

from app.routes.tax_routes import api as tax_namespace

api = Api()
api.add_namespace(tax_namespace)
