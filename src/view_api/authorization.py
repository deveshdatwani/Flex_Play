from werkzeug.security import check_password_hash
import mysql.connector 

def authorization(username, password):

	try:
		connector = mysql.connector.connect(,host='localhost',user='root',password='flexplay',database='flexplay')
		
		if connector.is_connected():
			cursor = connector.cursor()
			Player = cursor.execute('SELECT * from players WHERE player_username = username')
			
			if Player is not None:	
				player_info = cursor.fetchone()
				cursor.execute('SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "players"')
				columns = cursor.fetchone() 
				player_info_tuple = zip(columns, player_info)
				player = dict(player_info_tuple)

		if Player is None:
			response = "User not found"
			access = False
	
		elif not check_password_hash(player["password"], password):
			response = 'Incorrect password'
			access = False

		elif check_password_hash(player['password'], password):
			response = player 
			access = True

	return access, player