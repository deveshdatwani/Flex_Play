from flask import Blueprint
from flask import request
from random import randint
import mysql.connector

bp = Blueprint("create_group", __name__)

@bp.route("/create_group", methods=("GET", "POST"))
def login():

	if request.method == "POST":
		playerid = request.form["playerid"]
		groupname = request.form["groupname"]
		groupid = randint(100000,999999)
		connector = mysql.connector.connect(host='localhost',user='root',database='flexplay', auth_plugin='mysql_native_password')

	if connector.is_connected():
		cursor = connector.cursor(buffered=True)
		query = 'SELECT groupid FROM player_groups'
		cursor.execute(query)
		all_groupid = cursor.fetchall()

		while groupid in all_groupid:
			groupid = randint(1000000, 9999999)

		query = "INSERT INTO player_groups (playerid, groupid, admin) VALUES (%s, %s, %s);"
		val = playerid, groupid, True
		cursor.execute(query, val)
		connector.commit()

		query = "INSERT INTO group_master (groupid, groupname) VALUES (%s, %s)"
		val = groupid, groupname
		cursor.execute(query, val)
		connector.commit()

		cursor.close()
		connector.close()

	return "created group successfully"
