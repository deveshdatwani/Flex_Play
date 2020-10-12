from flask import Blueprint
from flask import request
from werkzeug.security import generate_password_hash
import mysql.connector
from random import randint

bp = Blueprint('register', __name__)

@bp.route("/register", methods=("GET", "POST"))
def register():

    if request.method == "POST":
        player_id = randint(1000000,9999999)
        username = request.form["username"]
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        emailid = request.form['email']
        phonenumber = request.form['phonenumber']
        password = generate_password_hash(request.form["password"])
        connector = mysql.connector.connect(host='localhost',user='root',database='flexplay', auth_plugin='mysql_native_password')

        if connector.is_connected():
            cursor = connector.cursor(buffered=True)
            query='SELECT playerid FROM player_master'
            all_playerid = cursor.execute(query)

            if all_playerid is not None:
                while playerid in all_playerid:
                    player_id = randint(1000000, 9999999)

            query = "INSERT INTO player_master (playerid, username, firstname, lastname, email, phonenumber, password) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            val = player_id, username, firstname, lastname, emailid, phonenumber, password
            cursor.execute(query, val)
            connector.commit()
            response = 'Created Account Successfully'
            cursor.close()
            connector.close()
    else:
        repsone = 'Cannot connect to database'

    return response
