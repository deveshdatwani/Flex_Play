from werkzeug.security import check_password_hash
from flask import Blueprint
from flask import request
from flask import jsonify
import mysql

bp = Blueprint("login", __name__)

def authorization(username, password):
	connector = mysql.connector.connect(host='localhost',user='root',database='flexplay')

	if connector.is_connected():
		cursor = connector.cursor()
		query = 'SELECT * FROM player_master WHERE username = "' + username + '"'
		cursor.execute(query)
		Player = cursor.fetchone()
		cursor.close()
		connector.close()

		if Player is not None:
			player_info = Player
			columns = ('playerid','username','password','firstname','lastname','email','phonenumber')
			player_info_tuple = zip(columns, player_info)
			player = dict(player_info_tuple)

	if Player is None:
		response = {'response':'Player not found'}
		access = {'access' : False}

	elif not check_password_hash(player["password"], password):
		response = {'response':'Incorrect password'}
		access = {'access' : False}

	elif check_password_hash(player['password'], password):
		response = player
		access = {'access' : True}

	return access, response


@bp.route("/login", methods=("GET", "POST"))
def login():

	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		access, response = authorization(username, password)

	else:
		return 'Retry with POST request'

	return jsonify({'access':access, 'response':response})
