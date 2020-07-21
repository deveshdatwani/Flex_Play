from flask import Blueprint
from flask import request
from flask import jsonify
from authorization import authorization

bp = Blueprint("player_home", __name__)

@bp.route("/player_home", methods=("GET", "POST"))
def player_home():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        location = request.form['location']
        player = None
        access, player = authorization(username, password)
    
    return player

