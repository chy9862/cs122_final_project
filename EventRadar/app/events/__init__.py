from app import db
from flask import render_template, request, flash, redirect
from app.models.models import Event

# will have all backend stuff -- processing json files and how we display data onto front end