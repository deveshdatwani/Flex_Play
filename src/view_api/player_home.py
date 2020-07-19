import functools
from flask import Blueprint
from flask import request
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from flask import jsonify

bp = Blueprint("player_home", __name__)

@bp.route("/player_home", methods=("GET", "POST"))
def login():
    """Log in a registered user by adding the user id to the session."""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        response = None
        user = db.execute(
            "SELECT * FROM user WHERE username = ?", (username,)
        ).fetchone()

        if user is None:
            response= "Incorrect username."
        
        elif not check_password_hash(user["password"], password):
            response= "Incorrect password."

        if response is None:
            response = jsonify(username)
        
    return response
