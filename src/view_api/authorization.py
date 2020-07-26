from werkzeug.security import check_password_hash
import mysql.connector 

def authorization(username, password):

	connector = mysql.connector.connect(user='root',database='flex_play',host='localhost',password='flexplay')
	
	player = None
	
	if player is None:
		response = "User not found"
		access = False
	
	elif not check_password_hash(player["password"], password):
		response = 'Incorrect password'
		access = False

	elif check_password_hash(player['password'], password):
		response = player 
		access = True

	return access, player