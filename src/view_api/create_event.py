from flask import Blueprint
from flask import request
from flask import jsonify
import mysql.connector

bp = Blueprint("create_event", __name__)

@bp.route('/create_event', methods=['GET','POST'])
def create_event():

    if request.method == "POST":
        creater = request.form['creater']
        player = request.form['player']
        daytime = request.form['daytime']
        eventarena = request.form['eventarena']
        location = request.form['location']
        team = request.form['team']
        #players = request.form['players']
        #timeslot = request.form['timeslot']
        privacy = request.form['privacy']
        gameplaytime = request.form['gameplaytime']
        connector = mysql.connector.connect(host='localhost',user='root',password='flexplay',database='flexplay')
    
        if connector.is_connected():
            cursor = connector.cursor(buffered=True)
            query = "INSERT INTO events_master(creater, player, daytime, eventarena, location, team, privacy, gameplaytime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);" 
            val = creater, player, daytime, eventarena, location, team, privacy, gameplaytime
            cursor.execute(query, val)
            connector.commit() 
            response = 'Created Event Successfully'
            cursor.close()
            connector.close()
       

    return response
