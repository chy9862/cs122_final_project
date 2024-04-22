import os

basedir = os.path.abspath(os.path.dirname(__file__))
DB_NAME = 'eventradar.db'
class Config:
    # Secret key for signing cookies and other security aspects
    SECRET_KEY = '\xcf[\xc27\xb5O^\xfa\xb0\xab\xc0\x12\x04t\xd8\xc5\x18\x14\xe0\x1f\xe4\xed7/'
    
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_NAME}'
    
    # + os.path.join(basedir, 'eventradar.db')
    
    # f'sqlite:///{DB_NAME}'
    # or \
    #     'sqlite:///' + os.path.join(basedir, 'eventradar.db')
    
    # For PostgreSQL, uncomment the line below and update with your details
    # SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/eventradar_db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Eventbrite API key
    EVENTBRITE_API_KEY = 'OD7MC3WOBIMIBOMYDQ'

    # Google OAuth Configurations (to be filled with your credentials)
    GOOGLE_CLIENT_ID = '410154457877-8lhj4gj2hivt4f6olrl54dkhsm0u53sf.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET =  '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'
    GOOGLE_DISCOVERY_URL = ('https://accounts.google.com/.well-known/openid-configuration')
