from flask import Blueprint
from flask import request
from flask import jsonify
import mysql.connector
import group_home

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
		group = ','.join(group)

	if group is not None:
		group = group.split(',')
		event_list = []
		string_list = []
		
		for player in group:
			query = 'SELECT creater,eventarena,daytime,gameplaytime FROM events_master WHERE creater = "' + player + '"'
			cursor.execute(query)
			event = cursor.fetchone()
			if event is not None:
				event_list.append(event)
		for i in event_list:
			for j in i:
				string_list.append(str(j))
				print(j)

		
	string_list = ','.join(string_list)
	cursor.close()
	connector.close()

	return string_list