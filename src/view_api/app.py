import os
import login, register, player_home, match_making, create_event, create_group, group_home
from flask import Flask

def create_app(test_config=None):
 
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    
    else:
        app.config.update(test_config)
  
    try:
        os.makedirs(app.instance_path)
    
    except OSError:
        pass

    app.register_blueprint(register.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(player_home.bp)
    app.register_blueprint(match_making.bp)
    app.register_blueprint(create_event.bp)
    app.register_blueprint(group_home.bp)
    app.register_blueprint(create_group.bp)

    return app

