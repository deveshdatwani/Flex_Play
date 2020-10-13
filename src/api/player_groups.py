from flask import Blueprint
from flask import request
from flask import jsonify
import mysql.connector

bp = Blueprint("groups", __name__)

@bp.route("/player_groups", methods=("GET", "POST"))
def login():

	if request.method == "POST":
		playerid = request.form['playerid']
		connector = mysql.connector.connect(host='localhost',user='root',database='flexplay')

		if connector.is_connected():
			cursor = connector.cursor()
			query = 'SELECT groupid, admin FROM player_groups WHERE playerid = "' + playerid + '"'
			cursor.execute(query)
			groups = cursor.fetchall()

			if groups is not None:

				player_groups = {}
				for group in groups:
					query = 'SELECT groupname FROM group_master WHERE groupid = "' + group + '"'
					cursor.execute(query)
					group_name = cursor.fetchone()
					player_groups[group] = group_name

			cursor.close()
			connector.close()

	return jsonify({'groups': player_groups})
