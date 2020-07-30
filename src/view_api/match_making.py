from flask import Blueprint
from flask import request
from flask import jsonify
import mysql.connector

bp = Blueprint("match_making", __name__)

def make_match(timeslot, location):
	connector = mysql.connector.connect(host='localhost',user='root',password='flexplay',database='flexplay')
	
	if connector.is_connected():
		privacy = 0
		cursor = connector.cursor()
		query = 'SELECT * FROM events_master WHERE timeslot = %s AND privacy = 0;'
		val = timeslot
		cursor.execute(query, (val,))
		events = cursor.fetchall()

	if events is None:
		response = "No events found"

	else:
		response = events
	
	cursor.close()
	connector.close() 

	return events

@bp.route("/match_making", methods=("GET", "POST"))
def match_making():   
	
	if request.method == "POST":
		location = request.form["location"]
		timeslot = request.form["timeslot"]   
    
	events = make_match(timeslot, location)
            
	return jsonify(events)
