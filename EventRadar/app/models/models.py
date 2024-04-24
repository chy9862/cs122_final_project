from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
#, login_manager

# User Loader for Flask-Login
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(20), index=True, nullable=False)
    password = db.Column(db.String(100), index=True, nullable=False)
    #relationship between user and event to store all events users sign up for. 
    event = db.relationship('Event')

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    location = db.Column(db.String(128), nullable=False)
    # 4/18/2024 @ 1:37 pm check if utcnow is causing any issues 
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created_at = db.Column(db.DateTime(timezone=True), index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))