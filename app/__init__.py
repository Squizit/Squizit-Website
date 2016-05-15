import remodel.connection
from flask import Flask
from flask_bcrypt import Bcrypt
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
try:
    remodel.connection.pool.configure(db='test', host='192.168.99.100', port=32769)
except:
    app.logger.critical('Database connection failed. Rethink Database must be running on configured host and port for app to start.')
    raise ConnectionError('Database connection failed. Rethink Database must be running on configured host and port for app to start.')

from app import routes
