#import os
import login
import login, register, player_home, match_making, create_event, groups, group_events, join_event, group_event, see_event_details, your_events, invite_player, see_your_notifications, group_home
from flask import Flask


app = Flask(__name__, instance_relative_config=True)

app.register_blueprint(register.bp)
app.register_blueprint(login.bp)
app.register_blueprint(player_home.bp)
app.register_blueprint(groups.bp)
app.register_blueprint(group_home.bp)
app.register_blueprint(group_event.bp)
app.register_blueprint(join_event.bp)
app.register_blueprint(create_event.bp)
#app.register_blueprint(delete_event.bp)
app.register_blueprint(match_making.bp)
#app.register_blueprint(group_event_home.bp)
app.register_blueprint(see_event_details.bp)
app.register_blueprint(your_events.bp)
app.register_blueprint(invite_player.bp)
app.register_blueprint(see_your_notifications.bp)


