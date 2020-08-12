from flask import Blueprint
from flask import request
from flask import jsonify
import mysql.connector

bp = Blueprint("see_your_notifications", __name__)

@bp.route("/see_your_notifications", methods=("GET", "POST"))
def login():

	if request.method == "POST":
		username = request.form['username']
		connector = mysql.connector.connect(host='localhost',user='root',password='flexplay',database='flexplay')
	
	if connector.is_connected():
		cursor = connector.cursor()
		query = 'SELECT invitor, team FROM notifications_master WHERE invited = "' + username + '"'
		cursor.execute(query)
		your_notifications = cursor.fetchall()
		cursor.close()
		connector.close()
		notifications = [str(x[0] + '-' + x[1] + ' -- ') for x in your_notifications]
		notifications = ''.join(notifications)
		print(notifications)

	return notifications