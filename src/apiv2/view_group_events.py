from flask import Blueprint
from flask import request
import mysql.connector
from flask import jsonify

bp = Blueprint('view_group_events', __name__)

@bp.route("/player_groups/group_home/view_group_events", methods=("GET", "POST"))
def register():

        if request.method == 'POST':
                groupid = request.form['groupid']
                connector = mysql.connector.connect(host='localhost',user='root',database='flexplay')
                cursor = connector.cursor()
                query = 'SELECT * FROM event_master'
                cursor.execute(query)
                all_events = cursor.fetchall()
                cursor.close()
                connector.close()

                return jsonify({'events':all_events})

        return 'No events'



