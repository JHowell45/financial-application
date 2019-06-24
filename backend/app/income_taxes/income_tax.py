"""Use this file for calculating the income tax.

This file contains the functions for calculating the income tax for a given user
income and returning both the leftover income tax and the income tax being paid.
"""

from .utils import create_tax_rate

TAX_BREAKDOWN = {
    "personal_allowance": create_tax_rate(upper_band=12500, tax_rate=0),
    "basic_rate": create_tax_rate(lower_band=12501, upper_band=50000, tax_rate=0.2),
    "higher_rate": create_tax_rate(lower_band=50001, upper_band=150000, tax_rate=0.4),
    "additional_rate": create_tax_rate(lower_band=150001, tax_rate=0.45),
}


def calculate_income_tax(income: int) -> float:
    """Use this function for calculating the income tax for the users income.

    This function is used for just calculating the income tax for a given income and
    returning both the income tax and the leftover income.

    :param income: the users pre-tax income.
    :return: the income tax and the leftover income for the user.
    """
    return 0
