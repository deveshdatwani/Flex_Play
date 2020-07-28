from werkzeug.security import check_password_hash
import mysql.connector 

def authorization(username, password):
	connector = mysql.connector.connect(host='localhost',user='root',password='flexplay',database='flexplay')
	
	if connector.is_connected():
		cursor = connector.cursor()
		query = 'SELECT * FROM players_master WHERE username = "' + username + '"'
		Player = cursor.execute(query)
		Player = cursor.fetchone()
		
		if Player is not None:
			player_info = Player 	
			columns = ('player_id','username','firstname','lastname','emailid','password','phonenumber','teamname')
			player_info_tuple = zip(columns, player_info)
			player = dict(player_info_tuple)

	if Player is None:
		response = "User not found"
		access = False

	elif not player["password"] ==  password:
		response = 'Incorrect password'
		access = False

	elif player['password'] == password:
		response = player 
		access = True
	
	cursor.close()
	connector.close() 

	return access, response