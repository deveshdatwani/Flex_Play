from flask import Blueprint
from flask import request
import mysql.connector

bp = Blueprint('remove_player_from_group', __name__)

@bp.route("/player_groups/group_home/remove_player_from_group", methods=("GET", "POST"))
def register():

        if request.method == 'POST':
                groupid = request.form['groupid']
                playerid = request.form['playerid']

                connector = mysql.connector.connect(host='localhost',user='root',database='flexplay')
                cursor = connector.cursor()
                query = 'DELETE FROM player_groups WHERE playerid = ' + playerid + ' AND groupid = ' + groupid
                cursor.execute(query)
                connector.commit()
                cursor.close()
                connector.close()

                return 'Removed player'

        return 'Couldnt delete player'
