from flask import Blueprint
from flask import request
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from authorization import authorization

bp = Blueprint("login", __name__)

@bp.route("/login", methods=("GET", "POST"))
def login():
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        access, player = authorization(username, password)
  
    return access, player