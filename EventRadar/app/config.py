import os

basedir = os.path.abspath(os.path.dirname(__file__))
DB_NAME = 'eventradar.db'
class Config:
    # Secret key for signing cookies and other security aspects
    SECRET_KEY = '\xcf[\xc27\xb5O^\xfa\xb0\xab\xc0\x12\x04t\xd8\xc5\x18\x14\xe0\x1f\xe4\xed7/'
    
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_NAME}'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ticketmaster API key
    api_key = "Zno3Ua2Uc6W4Am1IgDrW9osB2H6dnZct"
