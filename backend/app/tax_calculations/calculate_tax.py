"""Use this file for storing the functions used for calculating the tax on income.

This file contains the functions used for calculating the tax on income. Many of the
functions have shared utility and can be used for calculating several forms of tax,
which is why they are exported into specific functions here to reduce redundancy.
"""
from typing import List


def calculate_tax(
    income: float,
    tax_brackets: List[int],
    next_brackets: List[int],
    tax_rates: List[float],
):
    total_tax = 0
    for bracket, next_bracket, rate in generate_tax_sections(
        tax_brackets, next_brackets, tax_rates
    ):
        temp_tax, income = calculate_tax_for_bracket(
            income, bracket, next_bracket, rate
        )
        total_tax += temp_tax
    return round(total_tax, 2)


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


def generate_tax_sections(tax_brackets: list, next_bracket: list, tax_rates: list):
    """Use this function to calculate the rates and brackets for the tax sections.

    This function is used for returning the tax bracket, the following bracket to do
    subtractions to get the taxable amount and the tax rate for the bracket.

    :return: the tax bracket, the next bracket and the tax percentage.
    """

    for bracket, next_bracket, rate in zip(tax_brackets, next_bracket, tax_rates):
        yield bracket, next_bracket, rate
