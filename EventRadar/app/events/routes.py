#will have routes for the event pages 
from flask import Blueprint, render_template
from flask_login import current_user

events = Blueprint('events', __name__)

@events.route('/search')
def eventSearch():
    
    #this needs to have all events 
    return render_template('SearchEventPage.html', user=current_user)


#maybe take this one out
@events.route('/eventPage')
def eventPage():
    pass
# this needs to display 
