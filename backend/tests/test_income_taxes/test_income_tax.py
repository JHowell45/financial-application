"""

"""
import pytest

from app.tax_calculations.income_tax import calculate_income_tax


class TestIncomeTax:
    income_test_results = [
        (10000, 0),
        (25000, 2498.20),
        (50000, 7498.20),
        (100000, 27496),
        (500000, 204370.95),
    ]

    @pytest.mark.parametrize("income,income_tax", income_test_results)
    def test_result(self, income, income_tax):
        assert calculate_income_tax(income) == income_tax
