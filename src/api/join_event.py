from flask import Blueprint
from flask import request
from flask import jsonify
import mysql.connector

bp = Blueprint("join_event", __name__)

@bp.route('/player_home/groups/group_home/group_event/join_event', methods=['GET','POST'])
def join_event():

    if request.method == "POST":
        username = request.form['username']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        eventid = request.form['eventid']
        connector = mysql.connector.connect(host='us-cdbr-east-02.cleardb.com',user='be87857da36e44',password='665f4638',database='heroku_26cfe5af0cd58f4')
    
        if connector.is_connected():
            cursor = connector.cursor(buffered=True)
            query = "INSERT INTO event_players (username, firstname, lastname, eventid) VALUES (%s, %s, %s, %s);" 
            val = username, firstname, lastname, eventid
            cursor.execute(query, val)
            connector.commit() 
            cursor.close()
            connector.close()

    return 'Joined event'
