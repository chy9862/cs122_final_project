from flask import Blueprint, render_template
from app.models.models import db # check this later if it is an issue, nmight need to rename mdels.py to __init__.py
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

routes = Blueprint('routes', __name__)

@routes.route('/logout')
def logout():
    return '<h1>Logged out</h1>'

@routes.route('/')
def login():
    return '<h1>LoggedIn</h1>'
    
@routes.route('/sign-up')
def signUp():
    
    return render_template('SignUpPage.html')