"""Use this file to create a factory function for generating a Flask instance.

This file contains a function for creating a factory Flask application instance and
also initialising any of the extensions used by the application.
"""
from flask import Flask

from app.extensions import api, db
from config import Config


def create_app(config_class=Config):
    """Use this function to create an instance of the Flask application.

    This function is used as a factory function for creating an instance of the Flask
    application.

    :param config_class: the configuration class for the Flask application.
    :return: the factory Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    api.init_app(app)
    db.init_app(app)

    return app
