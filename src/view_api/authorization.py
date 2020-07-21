from werkzeug.security import check_password_hash

def authorization(username, password):

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