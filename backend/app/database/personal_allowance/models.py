"""Use this file for defining the database Models for this module.

This file contains the classes for defining the database tables for the personal
allowance tax information.
"""
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer

from app.extensions import db


class PersonalAllowance(db.Model):
    """Use this class for defining the database table for the personal allowance data.

    This class is used for defining the database table used for storing information
    on the personal allowances and the conditions for getting a specified amount.
    """

    financial_year = Column(Integer, nullable=True, unique=True)
    personal = Column()
    married_couple = Column()
    blind_person = Column()
    dividend = Column()
    savings_basic_rate = Column()
    savings_higher_rate = Column()
    personal_65_to_74 = Column()
    personal_over_75 = Column()
    married_couple_65_to_74 = Column()
    married_couple_over_75 = Column()
    income_limit = Column()
