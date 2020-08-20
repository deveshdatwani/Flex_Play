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
        latitude = request.form['latitude']
        longitude = request.form['longitude']
        team = request.form['team']
        privacy = request.form['privacy']
        gameplaytime = request.form['gameplaytime']
        connector = mysql.connector.connect(host='us-cdbr-east-02.cleardb.com',user='be87857da36e44',password='665f4638',database='heroku_26cfe5af0cd58f4')
    
        if connector.is_connected():
            cursor = connector.cursor(buffered=True)
            query = "INSERT INTO events_master(creater, player, daytime, eventarena, lat, lng, team, privacy, gameplaytime) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);" 
            val = creater, player, daytime, eventarena, latitude, longitude, team, privacy, gameplaytime
            cursor.execute(query, val)
            connector.commit() 
            response = {'response':'Created Event Successfully'}
            cursor.close()
            connector.close()
        else:
            response = {'response':'something went wrong'}
       

    return response
