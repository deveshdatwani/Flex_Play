import flask
from flas import jsonify, request

app = flask.Flask(__name__)
app.config[DEBUG] = True


# API FUNCTIONS FOR CREATING/DELETING A NEW PROFILE / REGISTER YOURSELF

""" Create a New Profile (CREATE) """ 

@app.route('/home/profile/settings/create_profile', methods=['POST'])
def create_new_profile():





""" Delete Your Profile (DELETE) """ 
 
@app.route('/home/profile/settings/delete_profile', methods=['POST'])
def delete_profile():








#API FUNCTIONS FOR LOGGING IN

""" Login from the login screen """

def valid_login(username_or_id, password):

	# Look for the profile with username
	# Check if the password is correct

	return login_attempt





def log_the_user_in(username_or_id):

	return 



@app.route('/login', methods=['POST', 'GET'])
def login():
    
    error = None    
    if request.method == 'POST':
        
        if valid_login(request.form['username'],request.form['password']):
            
            return log_the_user_in(request.form['username'])
        
        else:
            
            error = 'Invalid username/password'
   
    return render_template('login.html', error=error)




# API FUNCTIONS FOR AN INDIVIDUAL LOOKING FOR A SPOT

""" Home Page Profile Details Display  """

@app.route('/home/<username>', methods=['GET'])
def profile():







""" To Look For A Spot  """

@app.route('home/search/for/game', methods=['GET'])
def search_for_a_game():







""" Request a Spot in Play  """

@app.route('home/game/request', methods=['POST'])
def request_for_spot(): 


# ERROR PAGE DISPLAY

@app.errorhandler(404)
def page_not_found(error):
    
    return 'INVALID'