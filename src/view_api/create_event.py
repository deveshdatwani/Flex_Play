from flask import Blueprint
from flask import request
from flask import jsonify
import mysql.connector

bp = Blueprint("create_event", __name__)

@bp.route('/player_home/groups/group_home/create_group_event', methods=['GET','POST'])
def create_event():

    if request.method == "POST":
        creater = request.form['creater']
        username = request.form['username']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        event_arena = request.form['eventarena']
        play_time = request.form['playtime']
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        privacy = 1
        eventid = random.randit(100000,999999)
        date_time = request.form['daytime']
        connector = mysql.connector.connect(host='us-cdbr-east-02.cleardb.com',user='be87857da36e44',password='665f4638',database='heroku_26cfe5af0cd58f4')
    
        if connector.is_connected():
            cursor = connector.cursor(buffered=True)
            query = "INSERT INTO events_master (creater, eventarena, playtime, latitude, longitude, privacy, eventid, daytime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);" 
            val = creater, even_tarena, playtime, latitude, longitude, privacy, eventid, date_time
            cursor.execute(query, val)
            connector.commit() 
            query = "INSERT INTO events_players (username, firstname, lastname, eventid) VALUES (%s %s, %s, %s)"
            val = username, firstname, lastname, eventid
            cursor.execute(query, val)
            connector.commit()
            cursor.close()
            connector.close()
            response = 'response':'Created Event Successfully'
        else:
            response = 'response':'something went wrong'

    return response
