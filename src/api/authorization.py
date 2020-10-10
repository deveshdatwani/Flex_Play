from werkzeug.security import check_password_hash
import mysql.connector 

def authorization(username, password):
	connector = mysql.connector.connect(host='us-cdbr-east-02.cleardb.com',user='be87857da36e44',password='665f4638',database='heroku_26cfe5af0cd58f4')
	
	if connector.is_connected():
		cursor = connector.cursor()
		query = 'SELECT * FROM players_master WHERE username = "' + username + '"'
		cursor.execute(query)
		Player = cursor.fetchone()
		cursor.close()
		connector.close() 
		
		if Player is not None:
			player_info = Player 	
			columns = ('playerid','username','firstname','lastname','email','phonenumber','groupid','teamname','password')
			player_info_tuple = zip(columns, player_info)
			player = dict(player_info_tuple)

	if Player is None:
		response = {'response':'User not found'}
		access = {'access' : False}

	elif not check_password_hash(player["password"], password):
		response = {'response':'Incorrect password'}
		access = {'access' : False}

	elif check_password_hash(player['password'], password):
		response = player 
		access = {'access' : True}

	return access, response