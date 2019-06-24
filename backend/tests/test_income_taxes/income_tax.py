"""

"""
import pytest

from app.income_taxes.income_tax import calculate_income_tax


class TestIncomeTax:
    income_test_results = [(12500, 0)]

    @pytest.parametrize("income,income_tax", income_test_results)
    def test_result(self, income, income_tax):
        assert calculate_income_tax(income) == income_tax
