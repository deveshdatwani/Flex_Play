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
		connector = mysql.connector.connect(host='us-cdbr-east-02.cleardb.com',user='be87857da36e44',password='665f4638',database='heroku_26cfe5af0cd58f4')
	
	if connector.is_connected():
		cursor = connector.cursor(buffered=True)
		query = 'SELECT * FROM events_master WHERE creater = "' + creater + '"'
		cursor.execute(query)
		events = cursor.fetchall()
		cursor.close()
		connector.close()
		events = [[{'creater':x[0]},{'player':x[1]},
					{'date-time':x[2]},{'location':x[3]},
					{'group_name':x[4]},{'privacy':x[5]},
					{'in_out':x[6]},{'lat':x[7]},{'lng':x[8]}] for x in events]
		all_events = []
		
		for i, event in enumerate(events):
			all_events.append({'event{}'.format(i):event})
		
	return jsonify({'events' : all_events})
