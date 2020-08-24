from flask import Blueprint
from flask import request
from flask import jsonify
import mysql.connector

bp = Blueprint("group_event", __name__)

@bp.route("/player_home/groups/group_home/group_event", methods=("GET", "POST"))
def group_event_home():

	if request.method == "POST":
		eventid = request.form['eventid']
		connector = mysql.connector.connect(host='us-cdbr-east-02.cleardb.com',user='be87857da36e44',password='665f4638',database='heroku_26cfe5af0cd58f4')
	
	if connector.is_connected():
		cursor = connector.cursor(buffered=True)
		query = 'SELECT * FROM events_players WHERE creater = "' + eventid + '"'
		cursor.execute(query)
		event_players = cursor.fetchall()
		cursor.close()
		connector.close()
		players = []
		for player in event_players:
			players.append({'username':player[0], 'firstname':player[1], 'lastname':player[2]})
		
		
	return jsonify({'players' : players})
