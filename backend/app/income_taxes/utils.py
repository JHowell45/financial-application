"""Use the functions in this file for providing utility functionality to module.

This file contains functions for providing utility for the other functions for
calculating income taxes and other taxation's related to income for this module.
"""
from typing import Dict, Optional, Union


def create_tax_rate(
    tax_rate: float, lower_band: Optional[int] = None, upper_band: Optional[int] = None
) -> Dict[str, Union[int, float]]:
    """Use this function for generating the tax band rates for calculating income tax.

    This function is used for formatting an generating the income tax bands in the
    correct format.

    :param tax_rate: the percentage tax rate of this band.
    :param lower_band: the lowest income in this tax band.
    :param upper_band: the highest income in this tax band.
    :return: the formatted tax band.
    """
    return {"lower_band": lower_band, "upper_band": upper_band, "tax_rate": tax_rate}
