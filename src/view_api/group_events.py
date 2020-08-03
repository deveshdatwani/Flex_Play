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
		connector = mysql.connector.connect(host='localhost',user='root',password='flexplay',database='flexplay')
	
	if connector.is_connected():
		cursor = connector.cursor(buffered=True)
		query = 'SELECT teamname FROM players_master WHERE username = "' + username + '"'
		cursor.execute(query)
		teamname = cursor.fetchone()
		teamname = teamname[0]
		query = 'SELECT username FROM players_master WHERE teamname = "' + teamname + '"'
		cursor.execute(query)
		group = cursor.fetchall()
		#cursor.close()
		#connector.close()
		group = [x[0] for x in group]
		group = ','.join(group)
		print(group)

	if group is not None:
		group = group.split(',')
		
		for player in group:
			query = 'SELECT * FROM events_master WHERE creater = "' + player + '"'
			cursor.execute(query)
			event = cursor.fetchone()
			print(event)

	return 'Hey'
