"""Use this file for calculating the income tax.

This file contains the functions for calculating the income tax for a given user's
income and returning the tax being paid.
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


def calculate_income_tax(income: float) -> float:
    """Use this function for calculating the income tax for the users income.

    This function is used for just calculating the income tax for a given income and
    returning both the income tax and the leftover income.

    :param income: the users pre-tax income.
    :return: the income tax for the user.
    """
    total_tax = 0
    for bracket, next_bracket, rate in generate_tax_sections():
        temp_tax, income = calculate_tax_for_bracket(
            income, bracket, next_bracket, rate
        )
        total_tax += temp_tax
    return round(total_tax, 2)


def generate_tax_sections():
    """Use this function to calculate the rates and brackets for the tax sections.

    This function is used for returning the tax bracket, the following bracket to do
    subtractions to get the taxable amount and the tax rate for the bracket.

    :return: the tax bracket, the next bracket and the tax percentage.
    """
    tax_brackets = [ADDITIONAL_RATE, HIGHER_RATE_MIN, BASIC_RATE_MIN]
    next_bracket = [HIGHER_RATE_MAX, BASIC_RATE_MAX, PERSONAL_ALLOWANCE]
    tax_rates = [
        ADDITIONAL_RATE_PERCENTAGE,
        HIGHER_RATE_PERCENTAGE,
        BASIC_RATE_PERCENTAGE,
    ]
    for bracket, next_bracket, rate in zip(tax_brackets, next_bracket, tax_rates):
        yield bracket, next_bracket, rate


def calculate_tax_for_bracket(
    income: float, tax_bracket: int, next_bracket: int, tax_rate: float
):
    """Use this function to calculate the tax amount for a specific bracket.

    This function is used for calculating the tax amount for a specific tax bracket
    given the income.

    :param income: the income to tax.
    :param tax_bracket: the tax bracket being checked.
    :param next_bracket: the next bracket to only tax the specific amount.
    :param tax_rate: the tax rate for the given bracket.
    :return: the taxed amount and the new income amount to pass to following function.
    """
    if income >= tax_bracket:
        taxable_income = income - next_bracket
        taxed_amount = taxable_income * tax_rate
        return taxed_amount, next_bracket
    else:
        return 0, income
