from flask import Blueprint, render_template, request, flash
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
    
@routes.route('/sign-up', methods = ['GET', 'POST'])
def signUp():
    if request == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be larger than 5 characters', category='error')
        elif len(firstName) < 2:
            flash('First name must be larger than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords must match!', category='error')
        elif len(password1) < 8:
            flash('Password is too short. It should be larger than 7 characters', category='error')
        else:
            #create user into database
            pass
    return render_template('SignUpPage.html')