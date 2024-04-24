from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_migrate import Migrate
from app.config import Config
from os import path

# Create the database instance globally
db = SQLAlchemy()
DB_NAME = 'eventradar.db'
# Initialize login manager
login_manager = LoginManager()
# Login manager needs a view to redirect to when a login is required.
login_manager.login_view = 'auth.login'
# Initialize database migration tool
# migrate = Migrate()

def create_app(config_class=Config):
    # Initialize the app with the config from the config.py
    app = Flask(__name__)
    app.config.from_object(config_class)
    # secret key for cookies that will be generated in eventRadar
    app.config['SECRET_KEY'] = Config.SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    db.init_app(app)
    
    # login_manager = LoginManager()
    # login_manager.login_view = 'auth.login'
    # login_manager.init_app(app)
    # migrate.init_app(app, db)  # Initialize migrate with the app and db

    # Register Blueprints
    from app.auth import routes as routes_bp
    app.register_blueprint(routes_bp, url_prefix='/auth')
    
    from app.views import views as views_bp
    app.register_blueprint(views_bp, url_prefix='/')

    from app.models.models import User, Event
    
    with app.app_context():
        db.create_all()

    # @app.route('/')
    # def home():
    #     return render_template('index.html')
    
    
    # create_app(app)
    
    return app