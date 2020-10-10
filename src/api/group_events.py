from flask import Blueprint
from flask import request
from flask import jsonify
import mysql.connector

bp = Blueprint("group_events", __name__)

@bp.route("/group_events", methods=("GET", "POST"))
def group_events():

	if request.method == "POST":
		username = request.form['username']
		connector = mysql.connector.connect(host='us-cdbr-east-02.cleardb.com',user='be87857da36e44',password='665f4638',database='heroku_26cfe5af0cd58f4')
	
	if connector.is_connected():
		cursor = connector.cursor(buffered=True)
		query = 'SELECT teamname FROM players_master WHERE username = "' + username + '"'
		cursor.execute(query)
		teamname = cursor.fetchone()
		teamname = teamname[0]
		query = 'SELECT username FROM players_master WHERE teamname = "' + teamname + '"'
		cursor.execute(query)
		group = cursor.fetchall()
		group = [x[0] for x in group]
		all_group_players = []
		
		for i, player in enumerate(group):
			all_group_players.append({'player' : player})

	if group is not None:
		event_list = []
		
		for player in all_group_players:
			query = 'SELECT creater, eventarena, daytime, gameplaytime FROM events_master WHERE creater = "' + player['player'] + '"'
			cursor.execute(query)
			event = cursor.fetchone()
			if event is not None:
				event_list.append([{'creater' : event[0]}, {'eventarena' : event[1]}, {'daytime' : event[2]}, {'gameplaytime' : event[3]}])
		
	return jsonify({'events': event_list})