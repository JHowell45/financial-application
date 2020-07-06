"""Use this file for calculating the income tax.

This file contains the functions for calculating the income tax for a given user
income and returning both the leftover income tax and the income tax being paid.
"""

PERSONAL_ALLOWANCE = 12500
BASIC_RATE_MIN = 12501
BASIC_RATE_MAX = 50000
HIGHER_RATE_MIN = 50001
HIGHER_RATE_MAX = 150000
ADDITIONAL_RATE = 150001

BASIC_RATE_PERCENTAGE = 0.2
HIGHER_RATE_PERCENTAGE = 0.4
ADDITIONAL_RATE_PERCENTAGE = 0.45


def calculate_income_tax(pre_tax_income: int) -> float:
    """Use this function for calculating the income tax for the users income.

    This function is used for just calculating the income tax for a given income and
    returning both the income tax and the leftover income.

    :param pre_tax_income: the users pre-tax income.
    :return: the income tax for the user.
    """
    tax = 0
    if pre_tax_income >= ADDITIONAL_RATE:
        tax += (pre_tax_income - HIGHER_RATE_MAX) * ADDITIONAL_RATE_PERCENTAGE
        pre_tax_income = HIGHER_RATE_MAX
    if pre_tax_income >= HIGHER_RATE_MIN:
        tax += (pre_tax_income - BASIC_RATE_MAX) * HIGHER_RATE_PERCENTAGE
        pre_tax_income = BASIC_RATE_MAX
    if pre_tax_income >= BASIC_RATE_MIN:
        tax += (pre_tax_income - PERSONAL_ALLOWANCE) * BASIC_RATE_PERCENTAGE
    return tax
