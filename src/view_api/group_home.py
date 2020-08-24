from flask import Blueprint
from flask import request
from flask import jsonify
import mysql.connector

bp = Blueprint("group_home", __name__)

@bp.route("/player_home/groups/group_home", methods=("GET", "POST"))
def login():

	if request.method == "POST":
		groupid = request.form['groupid']
		connector = mysql.connector.connect(host='us-cdbr-east-02.cleardb.com',user='be87857da36e44',password='665f4638',database='heroku_26cfe5af0cd58f4')
	
		if connector.is_connected():
			cursor = connector.cursor()
			query = 'SELECT username FROM group_master WHERE groupid = "' + groupid + '"'
			cursor.execute(query)
			response = cursor.fetchall()
			group_players = []
			group_events = []
			
			for player in response:
				group_players.append({'username':player[0], 'firstname':player[1], 'lastname':player[2]})

			for player in group_players:
				player_username = player['username']
				query = 'SELECT * FROM events_master WHERE creater = "' + player_username + '"'
				cursor.execute(query)
				response = cursor.fetchall()

				for event in response:
					group_events.append({'creater':event[0], 'eventarena':event[1], 
										'playtime':event[2], 'latitude':event[3], 
										'longitude':event[4], 'privacy': event[5], 
										'eventid':event[6], 'datetime':event[7]})

			cursor.close()
			connector.close()
			print(group_players)
			print(group_events)
			
	return jsonify({'group_players':group_players, 'group_events':group_events})