from flask import Blueprint
from flask import request
from flask import jsonify
from authorization import authorization

bp = Blueprint("create_event", __name__)

@bp.route('player_home/create_event', methods=['GET','POST'])
def create_event():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        event_arena = request.form['eventarena']
        location = request.form['location']

        #-----------------------------------------------------------------

        #Add code to create a new 'Event' table in the SQL database

        #-----------------------------------------------------------------

    return new_event
