import functools
from flask import Blueprint
from flask import flash
from flask import request
from werkzeug.security import generate_password_hash
import mysql.connector
from random import randint

bp = Blueprint('register', __name__)

@bp.route("/register", methods=("GET", "POST"))
def register():

    if request.method == "POST":
        player_id = randint(10000000,99999999)
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        emailid = request.form['emailid']
        phonenumber = request.form['phonenumber']
        teamname = request.form['teamname']      
        connector = mysql.connector.connect(host='localhost',user='root',password='flexplay',database='flexplay')
    
        if connector.is_connected():
            cursor = connector.cursor(buffered=True)
            query = "INSERT INTO players_master (player_id, username, password, firstname, lastname, emailid, phonenumber, teamname) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);" 
            val = player_id, username, password, firstname, lastname, emailid, phonenumber, teamname
            cursor.execute(query, val)
            connector.commit() 
            response = 'Created Account Successfully'
            cursor.close()
            connector.close()
    else:
        repsone = 'Hello'

    return response