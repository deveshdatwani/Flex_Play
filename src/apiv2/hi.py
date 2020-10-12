from flask import Blueprint
from flask import render_template

bp = Blueprint("hi", __name__)

@bp.route("/", methods=("GET", "POST"))
def login():
    return  render_template('hello.html')
