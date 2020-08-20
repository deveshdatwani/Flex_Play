from flask import Blueprint
from flask import request
from flask import jsonify
import mysql.connector

bp = Blueprint("group_home", __name__)

@bp.route("/group_home", methods=("GET", "POST"))
def login():

	if request.method == "POST":
		username = request.form['username']
		connector = mysql.connector.connect(host='us-cdbr-east-02.cleardb.com',user='be87857da36e44',password='665f4638',database='heroku_26cfe5af0cd58f4')
	
	if connector.is_connected():
		cursor = connector.cursor()
		query = 'SELECT teamname FROM players_master WHERE username = "' + username + '"'
		cursor.execute(query)
		teamname = cursor.fetchone()
		teamname = teamname[0]
		query = 'SELECT username FROM players_master WHERE teamname = "' + teamname + '"'
		cursor.execute(query)
		group = cursor.fetchall()
		cursor.close()
		connector.close()
		group = [x[0] for x in group]
		all_players = []
		for i, player in enumerate(group):
			all_players.append({'player{}'.format(i):player})


	return jsonify({'group_players':all_players})