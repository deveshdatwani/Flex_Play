from flask import Blueprint
from flask import request
from flask import jsonify
import mysql.connector

bp = Blueprint("see_event_details", __name__)

@bp.route("/see_event_details", methods=("GET", "POST"))
def see_event_details():

	if request.method == "POST":
		event_creater = request.form['creater']
		daytime = request.form['daytime']
		connector = mysql.connector.connect(host='us-cdbr-east-02.cleardb.com',user='be87857da36e44',password='665f4638',database='heroku_26cfe5af0cd58f4')
	
	if connector.is_connected():
		cursor = connector.cursor(buffered =True)
		query = 'SELECT player FROM events_master WHERE creater = "' + event_creater + '"'
		cursor.execute(query)
		group = cursor.fetchall()
		players = []
		
		for player in group:
			players.append(player[0])

		event_players = ','.join(players)
	
	return event_players