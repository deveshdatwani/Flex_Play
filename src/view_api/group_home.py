from flask import Blueprint
from flask import request
from flask import jsonify

bp = Blueprint("group_home", __name__)

@bp.route("/group_home", methods=("GET", "POST"))
def login():

    if request.method == "POST":
        group_id = request.form['groupid']
    
        # --------------------------------------------------------------

        #Add code to fire a query to the SQL database in order to retrieve details of ALL players in the group table mentioned
        #Store the player details in variable called group

        # --------------------------------------------------------------
   
    return group
