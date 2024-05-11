"""Contains the routes for the application, including authentication routes.

This module contains the routes for the application, including the home route and the
login and sign-up routes. The routes are defined using the Flask Blueprint object.

Attributes:
    views: A Blueprint object that defines the routes for the application.

Typical usage example:
    return render_template("index.html", user=current_user)
"""

from flask import Blueprint, render_template
from flask_login import current_user

# Create a Blueprint object that defines the routes for the application
views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("index.html", user=current_user)
