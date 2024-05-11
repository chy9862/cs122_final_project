"""This file initializes the app and the database.

This file initializes the Flask app and the database. It also registers the blueprints
for the views and auth. The create_app function is used to create the app instance with
the specified configuration. The app context is used to create the database tables if
they do not exist.

Attributes:
    db: A SQLAlchemy object that represents the database.

Methods:
    create_app: A function that creates the app instance with the specified
        configuration.

Typical usage example:
    app = create_app()
    app.run(debug=True)
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.config import Config

# Create the database instance globally
db = SQLAlchemy()


def create_app(config_class=Config):
    """Initialize the app with the specified configuration class.

    This function initializes the Flask app with the specified configuration class. It
    sets the configuration options for the app, including the database URI and the secret
    key for cookies. The login manager is also initialized to handle user authentication.
    The app context is used to create the database tables if they do not exist.

    Args:
        config_class: A class representing the configuration options for the app.

    Returns:
        app: An instance of the Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Config.SQLALCHEMY_TRACK_MODIFICATIONS

    # Secret key for cookies that will be generated in eventRadar
    app.config["SECRET_KEY"] = Config.SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI

    # Initialize the database
    db.init_app(app)

    # Initialize login manager
    login_manager = LoginManager()
    login_manager.login_view = "views.home"  # Specify the login view
    login_manager.init_app(app)

    # Load user function for login manager
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # Import the blueprints
    from app.auth.views import routes as routes_bp
    from app.models.models import User
    from app.views import views as views_bp

    # Register the blueprints with the app
    app.register_blueprint(routes_bp, url_prefix="/auth")
    app.register_blueprint(views_bp, url_prefix="/")

    # Create the database tables if they do not exist
    with app.app_context():
        db.create_all()

    # Return the app instance
    return app
