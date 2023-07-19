from flask import Blueprint, render_template, request

from models.event import Event
from models.event_list import events

events_blueprint = Blueprint("events", __name__)
# GET /events
@events_blueprint.route('/events')
def index():
    return render_template('index.jinja', title='Events Page', event_list=events)

# POST /events
# creating a new event
@events_blueprint.route('/events', methods=['POST'])
def create_event():
    name = request.form["name"]
    date = request.form["date"]
    location = request.form["location"]
    number_of_guests = request.form["number_of_guests"]
    description = request.form["description"]
    event_recurring = request.form.get("recurring")
    new_event = Event(name, date, number_of_guests, location, description, event_recurring)
    events.append(new_event)
    return render_template('index.jinja', title='Events Page', event_list=events)
# get the fields from the form
# create the new event using the fields
# add the new event to the list of events
# return render template

# INDEX, display all events
