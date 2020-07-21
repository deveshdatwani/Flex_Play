from flask import Blueprint
from flask import request
from flask import jsonify
from random import choice

bp = Blueprint("match_making", __name__)

def make_match(time_slot, location):

    # --------------------------------------------------------------

    #Add code to fire a query to the SQL database in order to retrieve ALL events in the time slot store in the above variable
    #Store the table primary keys in a list called events

    # --------------------------------------------------------------

    return events

@bp.route("/match_making", methods=("GET", "POST"))
def login():
        
    events = make_match(time_slot, location)
    matched_event = choice(events)
            
    return matched_event
