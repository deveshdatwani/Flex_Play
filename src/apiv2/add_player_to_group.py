from flask import Blueprint
from flask import request
from flask import jsonify

bp = Blueprint("add_player_to_group", __name__)

bp.route('/player_groups/group_home/add_player_to_group', methods=('GET','POST'))
def add_player():

	if request.method == 'POST':
		groupid = request.form['groupid']
		playerid = request.form['playerid']

		connector = mysql.connector.connect(host='localhost',user='root',database='flexplay')
		cursor = conncector.cursor()
		query = 'INSERT INTO player_groups (playerid, groupid, admin) VALUES (%s, %s, %s)'
		values = playerid, groupid, 0
		cursor.execute(query, values)
		cursor.close()
		connector.close()

		return 'Added player'

	return 'Couldnt add player'
