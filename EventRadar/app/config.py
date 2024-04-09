import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Secret key for signing cookies and other security aspects
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-very-secret-key-change-it'

    # Database configuration
    # For SQLite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'eventradar.db')
    
    # For PostgreSQL, uncomment the line below and update with your details
    # SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/eventradar_db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Eventbrite API key
    EVENTBRITE_API_KEY = os.environ.get('EVENTBRITE_API_KEY') or 'your-eventbrite-api-key'

    # Google OAuth Configurations (to be filled with your credentials)
    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID') or 'your-google-client-id'
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET') or 'your-google-client-secret'
    GOOGLE_DISCOVERY_URL = ('https://accounts.google.com/.well-known/openid-configuration')
