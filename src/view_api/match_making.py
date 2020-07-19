import functools
from flask import Blueprint
from flask import request
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from flask import jsonify
from random import choice

bp = Blueprint("match_making", __name__)

@bp.route("/match_making", methods=("GET", "POST"))
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        time_slot = request.form['timeslot']
        player = None
    
    # ------------------------------------------------------------- 


    #Add code to fire a query to the SQL database in order to retrieve user iformation from user's username
    #Store the information in the object player


    # ------------------------------------------------------------------------

        
        #Authenticate user credentials before returning user information

        if player is None:
            response= "User not found"
        
        elif not check_password_hash(player["password"], password):
            response = 'Incorrect password'

        elif check_password_hash(player['password'], password):
            
            # --------------------------------------------------------------

            #Add code to fire a query to the SQL database in order to retrieve ALL events in the time slot store in the above variable
            #Store the table primary keys in a list called events


            # --------------------------------------------------------------

            matched_event = rchoice(events)
            return matched_event



    return 'Match Making'
