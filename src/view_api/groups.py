from flask import Blueprint
from flask import request
from flask import jsonify
import mysql.connector

bp = Blueprint("groups", __name__)

@bp.route("/player_home/groups", methods=("GET", "POST"))
def login():

	if request.method == "POST":
		username = request.form['username']
		connector = mysql.connector.connect(host='us-cdbr-east-02.cleardb.com',user='be87857da36e44',password='665f4638',database='heroku_26cfe5af0cd58f4')
	
		if connector.is_connected():
			cursor = connector.cursor()
			query = 'SELECT groupid, groupname FROM groups_master WHERE username = "' + username + '"'
			cursor.execute(query)
			groups = cursor.fetchall()
			cursor.close()
			connector.close()
			group_info = []
			
			for group in groups:
				group_info.append({'groupid': group[0], 'groupname': group[1]})
			
	return jsonify({'groups': group_info})