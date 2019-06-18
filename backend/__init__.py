"""

"""
from flask import Flask
from backend.config import Config


def create_app(config_class=Config):
    """Use this function to create an instance of the Flask application.

    This function is used as a factory function for creating an instance of the Flask
    application.

    :param config_class: the configuration class for the Flask application.
    :return: the factory Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    return app
