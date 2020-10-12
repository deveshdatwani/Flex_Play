from flask import Flask
import register, hi, login

app = Flask(__name__, instance_relative_config=True)

app.register_blueprint(register.bp)
app.register_blueprint(hi.bp)
app.register_blueprint(login.bp)
