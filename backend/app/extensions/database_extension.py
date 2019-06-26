"""Use this file for creating a handler instance for the database."""
from flask_sqlalchemy import Model, SQLAlchemy
from inflection import underscore
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer


class BaseModel(Model):
    """Use this Mixin for providing the base database Columns and functions.

    This database mixin provides the database Columns or functions for all of the
    database Model classes that inherit this Mixin.
    """

    @declared_attr
    def __tablename__(cls):
        """Use this function to provide the table name for the database Model classes.

        This function is used for generating the database table name for the database
        Model class that inherits this Mixin.

        :return: the database table name.
        """
        return underscore(cls.__name__).replace("_table", "")

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        """Use this function to create representation for the inheriting database Model.

        This function is used for generating the representation for the database
        Model classes. It can generate it for each Model without any overriding
        required.

        :return: the database Model instance representation.
        """
        class_representation = f"<{self.__class__.__name__}"
        for attr in self.__table__.c.keys():
            class_representation += ", "
            value = getattr(self, attr)
            attr_title = attr.title().replace("_", " ").replace("Id", "ID")
            if isinstance(value, str):
                attr_representation = f'{attr_title}: "{value}"'
            else:
                attr_representation = f"{attr_title}: {value}"
            class_representation += attr_representation
        class_representation += ">"
        return class_representation


db = SQLAlchemy(model_class=BaseModel)
