from flask import Blueprint
from flask import request
from flask import jsonify
import mysql.connector

bp = Blueprint("create_event", __name__)

@bp.route('/player_home/create_event', methods=['GET','POST'])
def create_event():

    if request.method == "POST":
        creater = request.form["creater"]
        event_arena = request.form['eventarena']
        location = request.form['location']
        team = request.form['team']
        players = request.form['players']
        timeslot = request.form['timeslot']
        connector = mysql.connector.connect(host='localhost',user='root',password='flexplay',database='flexplay')
    
        if connector.is_connected():
            cursor = connector.cursor(buffered=True)
            query = "INSERT INTO events_master (creater, eventarena, location, team, players, timeslot) VALUES (%s, %s, %s, %s, %s, %s);" 
            val = creater, event_arena, location, team, players, timeslot
            cursor.execute(query, val)
            connector.commit() 
            response = 'Created Event Successfully'
            cursor.close()
            connector.close()
       

    return response
