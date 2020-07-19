import functools
from flask import Blueprint
from flask import flash
from flask import request
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from flask import jsonify

bp = Blueprint("player_home", __name__)

@bp.route("/player_home", methods=("GET", "POST"))
def login():
    """Log in a registered user by adding the user id to the session."""
    error = 'Player Home'
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None
        user = db.execute(
            "SELECT * FROM user WHERE username = ?", (username,)
        ).fetchone()

        if user is None:
            error = "Incorrect username."
        
        elif not check_password_hash(user["password"], password):
            error = "Incorrect password."

        if error is None:
            error = jsonify(username, password)
        
    return error
