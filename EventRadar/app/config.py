"""Configuration file for the app

This file contains the configuration options for the app. The Config class
contains the configuration options for the app, including the secret key for
cookies and the database URI. The configuration options are set as class
attributes.

Attributes:
    basedir: A string representing the base directory of the app.

Typical usage example:
    app.config.from_object(Config)
    app.config["SECRET_KEY"] = Config.SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Contains the configuration options for the app.

    This class contains the configuration options for the app, including the
    secret key for cookies and the database URI. The configuration options are
    set as class attributes.

    Attributes:
        SECRET_KEY: A string representing the secret key for cookies.
        SQLALCHEMY_DATABASE_URI: A string representing the URI for the database.
        SQLALCHEMY_TRACK_MODIFICATIONS: A boolean representing whether to track
            modifications.

    """

    SECRET_KEY = (
        "\xcf[\xc27\xb5O^\xfa\xb0\xab\xc0\x12\x04t\xd8\xc5\x18\x14\xe0\x1f\xe4\xed7/"
    )

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{'eventradar.db'}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Ticketmaster API key
    API_KEY = "Zno3Ua2Uc6W4Am1IgDrW9osB2H6dnZct"
