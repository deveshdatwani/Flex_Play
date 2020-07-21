from flask import Blueprint
from flask import request
from flask import jsonify

bp = Blueprint("create_group", __name__)

@bp.route("/create_group", methods=("GET", "POST"))
def login():

    if request.method == "POST":
        #This request should take artibitary number of player usernames
        player_user_name = request.form['playerusername']
        group_name = request.form['groupname']
		    
        # --------------------------------------------------------------

        #Add code to create a group in the SQL database and 

        # --------------------------------------------------------------
   
    return group
