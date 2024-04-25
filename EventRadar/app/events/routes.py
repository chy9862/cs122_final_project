#will have routes for the event pages 
from flask import Blueprint

events = Blueprint('events', __name__)

@events.route('/eventSearch')
def eventSearch():
    pass

@events.route('/eventPage')
def eventPage():
    pass
