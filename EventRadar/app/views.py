from flask import Blueprint, render_template, request, flash, Flask
views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('index.html')
