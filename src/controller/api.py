import flask
from flas import jsonify, request

app = flask.Flask(__name__)
app.config[DEBUG] = True


# API FUNCTIONS FOR AN INDIVIDUAL LOOKING FOR A SPOT

""" Home Page Display """

@app.route('/home', methods=['GET'])
def profile():








""" To Look For A Spot  """

@app.route('home/search/for/game', methods=['GET'])
def search_for_a_game():







""" Request a Spot in Plauy """

@app.route('home/game/request', methods=['POST'])
def request_for_spot(): 