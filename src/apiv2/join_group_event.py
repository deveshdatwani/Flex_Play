from flask import Blueprint
from flask import request
import mysql.connector
from flask import jsonify

bp = Blueprint('join_group_event', __name__)

@bp.route("/player_groups/group_home/join_group_event", methods=("GET", "POST"))
def register():

        if request.method == 'POST':
                groupid = request.form['groupid']
                playerid = request.form['playerid']
                connector = mysql.connector.connect(host='localhost',user='root',database='flexplay')
                cursor = connector.cursor()
                query = 'INSERT INTO event_players (playerid, eventid) VALUES (%s, %s)'
                values = groupid, playerid
                cursor.execute(query, values)
                connector.commit()
                cursor.close()
                connector.close()

                return 'Joined Event'

        return 'No events'
