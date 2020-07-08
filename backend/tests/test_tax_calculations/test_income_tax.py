"""

"""
import pytest

from app.tax_calculations import calculate_income_tax, calculate_national_insurance


class TestIncomeTax:
    income_test_results = [
        (10000, 0),
        (25000, 2498.20),
        (50000, 7498.20),
        (100000, 27498.2),
        (500000, 204998.2),
    ]

    @pytest.mark.parametrize("income,income_tax", income_test_results)
    def test_result(self, income, income_tax):
        assert calculate_income_tax(income) == income_tax


class TestNationalInsurance:
    income_test_results = [
        (10000, 60),
        (25000, 1860),
        (50000, 4860),
        (100000, 5860),
        (500000, 13860),
    ]

    @pytest.mark.parametrize("income,national_insurance", income_test_results)
    def test_result(self, income, national_insurance):
        assert calculate_national_insurance(income) == national_insurance
