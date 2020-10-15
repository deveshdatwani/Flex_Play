from flask import Blueprint
from flask import request
import mysql.connector
from random import randint

bp = Blueprint('create_event', __name__)

@bp.route("/player_groups/group_home/create_event", methods=("GET", "POST"))
def register():

        if request.method == 'POST':
                groupid = request.form['groupid']
                playerid = request.form['playerid']
                creator = playerid
                playtime = request.form['playerid']
                date = request.form['datetime']
                eventname = request.form['eventname']
                maxplayers = request.form['maxplayers']
                groupid = request.form['groupid']
                eventid = randint(10000,99999)
                connector = mysql.connector.connect(host='localhost',user='root',database='flexplay')
                cursor = connector.cursor()
                query = 'SELECT eventid FROM event_master'
                cursor.execute(query)
                all_event_id = cursor.fetchall()
                print(all_event_id)
                print(eventid in all_event_id)

                while eventid in all_event_id:
                    eventid = randint(10000,99999)

                query = 'INSERT INTO event_master (eventid, playtime, maxplaers, date, creator, eventname, groupid) VALUES (%s, %s, %s, %s, %s, %s, %s)'
                values = eventid, playtime, maxplayers, date, creator, eventname, groupid
                cursor.execute(query, values)
                connector.commit()
                cursor.close()
                connector.close()

                return 'Created event'

        return 'Couldnt create event. Something went wrong'

