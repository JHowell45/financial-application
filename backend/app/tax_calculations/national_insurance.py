"""Use this file for calculating the NI tax.

This file contains the functions for calculating the national insurance for a given
user's income and returning the national insurance being paid.
"""


def calculate_national_insurance(income: float):
    monthly_income = income / 12
