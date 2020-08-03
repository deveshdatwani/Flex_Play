from flask import Blueprint
from flask import request
from flask import jsonify
import mysql.connector
import group_home

bp = Blueprint("group_event_home", __name__)

@bp.route("/group_event_home", methods=("GET", "POST"))
def group_event_home():

	if request.method == "POST":
		creater = request.form['creater']
		connector = mysql.connector.connect(host='localhost',user='root',password='flexplay',database='flexplay')
	
	if connector.is_connected():
		cursor = connector.cursor(buffered=True)
		query = 'SELECT * FROM events_master WHERE creater = "' + creater + '"'
		cursor.execute(query)
		group = cursor.fetchall()
		print(group)
		
	return 'Hey'
