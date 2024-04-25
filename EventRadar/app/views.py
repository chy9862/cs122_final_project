from flask import Blueprint, render_template, request, flash, Flask
from app import create_app
views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('index.html')

@views.route('/authorizedHome')
def authorizedHome():
    return render_template('index.html')
