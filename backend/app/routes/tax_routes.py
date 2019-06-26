"""Use this file to create API endpoints for calculating taxes.

This file contains API endpoints that are used for calculating the taxes for an
individual and returning the amount left over and the taxes paid and the taxes break
down.
"""
from flask_restplus import Namespace, Resource

from app.tax_calculations import calculate_income_tax

api = Namespace(
    "taxes",
    description=(
        "API endpoints for returning taxes, money left over and a break down of the "
        "taxes being paid."
    ),
)


@api.route("/income/<int:income>")
class IncomeTaxes(Resource):
    """Use this API endpoint to calculate the taxes for the users income.

    This class is used for creating an API endpoint for calculating the leftover
    income for the user and returning the tax breakdown too.
    """

    def get(self, income):
        """Use this function to get the results of calculating the income taxes.

        This function returns the income, leftover income and the breakdown of the
        taxes coming out of the pre-tax income.

        :param income: the users income.
        :return: the income, leftover income and the tax breakdown.
        """
        return {
            "total_income": income,
            "national_insurance": 0,
            "leftover_income": 0,
            "income_tax": calculate_income_tax(),
            "university_repayments": 0,
        }
