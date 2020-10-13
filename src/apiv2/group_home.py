from flask import Blueprint
from flask import request
from flask import jsonify
import mysql.connector

bp = Blueprint("group_home", __name__)

@bp.route('/player_groups/group_home', methods=('GET','POST'))
def group_home():

	if request.method == 'POST':
		groupid = request.form['groupid']

	connector = mysql.connector.connect(host='localhost',user='root',database='flexplay')
	cursor = connector.cursor()
	query = 'SELECT playerid FROM player_groups WHERE groupid = ' + groupid
	cursor.execute(query)
	group_players = cursor.fetchall()
	print(group_players)
	group_players = group_players[0]
	query = 'SELECT groupname FROM group_master WHERE groupid = ' + groupid
	cursor.execute(query)
	group_name = cursor.fetchone()
	group_name = ''.join(group_name)

	if len(group_players) != 0:
		players = {}
		columns = ['username','firstname','lastname','email','phonenumber']

		for player in group_players:
			query = 'SELECT username, firstname, lastname, email, phonenumber FROM player_master WHERE playerid = ' + player
			cursor.execute(query)
			group_player = cursor.fetchone()
			player_info = zip(columns, group_player)
			player_info = dict(player_info)

	players[player] = player_info
	cursor.close()
	connector.close()

	return jsonify({'group_name':group_name, 'group_players':players})
