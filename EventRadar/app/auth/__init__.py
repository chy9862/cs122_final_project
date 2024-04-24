from flask import Blueprint, render_template, request, flash, redirect, url_for
from app import db # check this later if it is an issue, nmight need to rename mdels.py to __init__.py
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.models import User

routes = Blueprint('routes', __name__)

@routes.route('/logout')
# @login_required
def logout():
    # logout_user()
    return render_template('/')

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        #checks if user exist through email. Then use check_password_hash() to check if password matches with password from request
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Loggin in successfully.', category='success')
                login_user(user, remember=True)
                return redirect('views.home') # change this later
            else:
                flash('Password does not match. Try Again.', category='error')
        else:
            flash('Email does not exist.', category='error')
            
    return render_template('LoginPage.html', user = current_user)
    
@routes.route('/sign-up', methods = ['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be larger than 3 characters', category='error')
        elif len(first_name) < 2:
            flash('First name must be larger than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords must match!', category='error')
        elif len(password1) < 8:
            flash('Password is too short. It should be larger than 7 characters', category='error')
        else:
            #generates a password hash with sha-256 algorithm as a security feature.
            new_user = User(email = email, first_name = first_name, password = generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created successfully!', category='success')
            # return redirect(url_for('views.authorizedHome'))
        
    return render_template('SignUpPage.html', user = current_user)