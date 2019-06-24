"""Use this file to create API endpoints for calculating taxes.

This file contains API endpoints that are used for calculating the taxes for an
individual and returning the amount left over and the taxes paid and the taxes break
down.
"""
from flask_restplus import Namespace, Resource

api = Namespace(
    "taxes",
    description=(
        "API endpoints for returning taxes, money left over and a break down of the "
        "taxes being paid."
    ),
)


@api.route("/income")
class IncomeTaxes(Resource):
    def get(self):
        pass
