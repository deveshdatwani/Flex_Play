from flask import Blueprint
from flask import request
import mysql.connector

bp = Blueprint('add_player_to_group', __name__)

@bp.route("/player_groups/group_home/add_player_to_group", methods=("GET", "POST"))
def register():

	if request.method == 'POST':
		groupid = request.form['groupid']
		playerid = request.form['playerid']

		connector = mysql.connector.connect(host='localhost',user='root',database='flexplay')
		cursor = connector.cursor()
		query = 'INSERT INTO player_groups (playerid, groupid, admin) VALUES (%s, %s, %s)'
		values = playerid, groupid, 0
		cursor.execute(query, values)
		connector.commit()
		cursor.close()
		connector.close()

		return 'Added player'

	return 'Couldnt add player'
