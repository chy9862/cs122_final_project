"""Contains the routes for the application, including authentication routes.

This module contains the routes for the application, including the home route and the
login and sign-up routes. The routes are defined using the Flask Blueprint object.

Attributes:
    app: A Blueprint object that defines the routes for the application.

Typical usage example:
    return render_template("index.html", user=current_user)
"""

from flask import Blueprint, render_template
from flask_login import current_user

# Create a Blueprint object that defines the routes for the application
main = Blueprint("main", __name__)


@main.route("/")
def home():
    """Renders the home page of the application.

    This function renders the home page of the application, which is the landing page
    when the user first visits the site. It returns the rendered template with the
    current user object.

    Returns:
        A rendered template with the current user object.
    """
    return render_template("index.html", user=current_user)
