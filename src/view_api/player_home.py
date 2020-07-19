import functools
from flask import Blueprint
from flask import request
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from flask import jsonify

bp = Blueprint("player_home", __name__)

@bp.route("/player_home", methods=("GET", "POST"))
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
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
            response = player
        
    return response
