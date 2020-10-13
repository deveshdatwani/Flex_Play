from flask import Flask
import register, hi, login, player_groups, create_group, group_home, add_player_to_group

app = Flask(__name__, instance_relative_config=True)

app.register_blueprint(register.bp)
app.register_blueprint(hi.bp)
app.register_blueprint(login.bp)
app.register_blueprint(player_groups.bp)
app.register_blueprint(create_group.bp)
app.register_blueprint(group_home.bp)
app.register_blueprint(add_player_to_group.bp)
