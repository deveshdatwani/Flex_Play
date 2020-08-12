from flask import Blueprint
from flask import request
from flask import jsonify
import mysql.connector

bp = Blueprint("your_events", __name__)

@bp.route("/your_events", methods=("GET", "POST"))
def login():

	if request.method == "POST":
		username = request.form['username']
		connector = mysql.connector.connect(host='localhost',user='root',password='flexplay',database='flexplay')
	
	if connector.is_connected():
		cursor = connector.cursor()
		query = 'SELECT creater,eventarena,daytime,gameplaytime FROM events_master WHERE player = "' + username + '"'
		cursor.execute(query)
		your_events = cursor.fetchall()
		cursor.close()
		connector.close()
		print(your_events)
		print(len(your_events))
		print(type(your_events))


	return 'Hi'
