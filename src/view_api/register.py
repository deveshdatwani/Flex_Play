import functools
from flask import Blueprint
from flask import flash
from flask import request
from werkzeug.security import generate_password_hash

bp = Blueprint('register', __name__)

@bp.route("/register", methods=("GET", "POST"))
def register():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
    '''

    Create a user in the SQL database with the username and password in above variables
    Use generate_password_hash function to encrypt password


    '''  

        return 'Created Account Succesfully'

    else:
        return None