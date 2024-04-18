from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_migrate import Migrate
from app.config import Config
from authlib.integrations.flask_client import OAuth  # Include this if you're planning to use OAuth

# Create the database instance globally
db = SQLAlchemy()
# Initialize login manager
login_manager = LoginManager()
# Initialize the OAuth instance
oauth = OAuth()
# Login manager needs a view to redirect to when a login is required.
login_manager.login_view = 'auth.login'
# Initialize database migration tool
# migrate = Migrate()

def create_app(config_class=Config):
    # Initialize the app with the config from the config.py
    app = Flask(__name__)
    app.config.from_object(config_class)
    # secret key for cookies that will be generated in eventRadar
    app.config['SECRET_KEY']

    # Initialize extensions with the application
    # db.init_app(app)
    # login_manager.init_app(app)
    # oauth.init_app(app)  # Initialize OAuth with the app
    # migrate.init_app(app, db)  # Initialize migrate with the app and db

    # Register Blueprints
    from app.auth import routes as routes_bp
    app.register_blueprint(routes_bp, url_prefix='/auth')

    # from app.events import events as events_blueprint
    # app.register_blueprint(events_blueprint, url_prefix='/events')

    # from app.user import user as user_blueprint
    # app.register_blueprint(user_blueprint, url_prefix='/user')

    # A simple homepage route, can be expanded or replaced as needed
    @app.route('/')
    def home():
        return render_template('index.html')
    
    
    return app
