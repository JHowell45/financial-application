"""Use this file to create API endpoints for calculating taxes.

This file contains API endpoints that are used for calculating the taxes for an
individual and returning the amount left over and the taxes paid and the taxes break
down.
"""
from flask_restplus import Namespace, Resource, reqparse

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
        parser = reqparse.RequestParser()
        parser.add_argument(
            "income", type=int, help="Your pre-tax income or salary for an entire year."
        )
        args = parser.parse_args()
        return {
            "total_income": args["income"],
            "national_insurance": 0,
            "leftover_income": 0,
            "income_tax": 0,
            "university_repayments": 0,
        }
