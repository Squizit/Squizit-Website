import remodel.connection
from flask import Flask
from flask.ext.bcrypt import Bcrypt
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
socketio = SocketIO(app)
login = LoginManager()
login.init_app(app)
csrf = CsrfProtect(app)
bcrypt = Bcrypt(app)
remodel.connection.pool.configure(db='test', host='localhost', port=28015)

from app import routes
