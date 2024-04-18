from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)


@routes.route('/logout')
def logout():
    return '<h1>Logged out</h1>'

@routes.route('/')
def login():
    # return '<h1>LoggedIn</h1>'
    return render_template('home.html')
    
@routes.route('/sign-up')
def signUp():
    return '<h1>SignUp</h1>'