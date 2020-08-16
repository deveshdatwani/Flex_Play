from flask import Blueprint
from flask import request
from authorization import authorization
from flask import jsonify

bp = Blueprint("login", __name__)

@bp.route("/login", methods=("GET", "POST"))
def login():
    
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		print(username, password)
		access, response = authorization(username, password)

	else:
		response = 'Hi'

	return jsonify(access, response)
