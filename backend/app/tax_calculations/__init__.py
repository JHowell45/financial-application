"""

"""
from .calculate_tax import calculate_tax


def calculate_income_tax(income: float) -> float:
    """Use this function for calculating the income tax for the users income.

    This function is used for just calculating the income tax for a given income and
    returning both the income tax and the leftover income.

    :param income: the users pre-tax income.
    :return: the income tax for the user.
    """
    PERSONAL_ALLOWANCE = 12509
    BASIC_RATE_MIN = 12510
    BASIC_RATE_MAX = 50000
    HIGHER_RATE_MIN = 50001
    HIGHER_RATE_MAX = 150000
    ADDITIONAL_RATE = 150001

    BASIC_RATE_PERCENTAGE = 0.2
    HIGHER_RATE_PERCENTAGE = 0.4
    ADDITIONAL_RATE_PERCENTAGE = 0.45

    tax_brackets = [ADDITIONAL_RATE, HIGHER_RATE_MIN, BASIC_RATE_MIN]
    next_brackets = [HIGHER_RATE_MAX, BASIC_RATE_MAX, PERSONAL_ALLOWANCE]
    tax_rates = [
        ADDITIONAL_RATE_PERCENTAGE,
        HIGHER_RATE_PERCENTAGE,
        BASIC_RATE_PERCENTAGE,
    ]
    return calculate_tax(income, tax_brackets, next_brackets, tax_rates)


def calculate_national_insurance(income: float) -> float:
    """Use this function for calculating the national insurance for the users income.

    This function is used for just calculating the national insurance for a given
    income and returning both the national insurance and the leftover income.

    :param income: the users pre-tax income.
    :return: the national insurance for the user.
    """
    EXEMPT = 9500
    BASE_BRACKET_MIN = 9501
    BASE_BRACKET_MAX = 50000
    MAX_EMPLOYED_BRACKET = 50001

    BASE_RATE = 0.12
    MAX_RATE = 0.02
    tax_brackets = [MAX_EMPLOYED_BRACKET, BASE_BRACKET_MIN]
    next_brackets = [BASE_BRACKET_MAX, EXEMPT]
    tax_rates = [MAX_RATE, BASE_RATE]
    return calculate_tax(income, tax_brackets, next_brackets, tax_rates)
