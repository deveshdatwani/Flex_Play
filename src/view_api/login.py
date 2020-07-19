from flask import Blueprint
from flask import request
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

bp = Blueprint("login", __name__)

@bp.route("/login", methods=("GET", "POST"))
def login():
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        player = None
    
    ''' 

    Add code to fire a query to the SQL database in order to retrieve user iformation from user's username
    Store the information in the object player
    Use generate_password_hash on password before using check_password_hash

    '''

        #Authentication

        if player is None:
            response= "User not found"
        
        elif not check_password_hash(player["password"], password):
            response = 'Incorrect password'

        elif check_password_hash(player['password'], password):
            response = 'Login Succesfull'
        
    return response
