from flask import Blueprint
from flask import request
from flask import jsonify
import mysql.connector

bp = Blueprint("invite_player", __name__)

@bp.route("/invite_player", methods=("GET", "POST"))
def login():

	if request.method == "POST":
		invited = request.form['invited']
		invitor = request.form['invitor']
		team = request.form['team']
		connector = mysql.connector.connect(host='us-cdbr-east-02.cleardb.com',user='be87857da36e44',password='665f4638',database='heroku_26cfe5af0cd58f4')
	
	if connector.is_connected():
		cursor = connector.cursor()
		query = 'INSERT INTO notifications_master(invitor, team, invited) VALUES (%s, %s, %s);'
		val = invitor, team, invited
		cursor.execute(query, val)
		connector.commit()
		cursor.close()
		connector.close()
       

	return 'Invited'
