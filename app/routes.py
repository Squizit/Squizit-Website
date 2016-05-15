from flask import render_template
from flask_login import current_user, login_user, login_required
from flask_wtf.csrf import validate_csrf

from app import app, login, socketio, csrf, bcrypt
from app.models import User


@app.before_request
def check_csrf():
    csrf.protect()


@login.user_loader
def load_user(user_id):
    return User.get(id=id)


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/adduser')
def adduser():
    return render_template('adduser.html')


@socketio.on('connect')
def connect_handler():
    if current_user.is_authenticated:
        socketio.emit('sb', 'Hello ' + current_user['name'] + '!')
    else:
        pass


@socketio.on('login user')
def user_form(json):
    if validate_csrf(json['json']['csrf']):
        user = User.get(email=json['json']['email'])
        socketio.emit('login user response')
        if user is not None:
            if bcrypt.check_password_hash(user['password'], json['json']['password']):
                login_user(user)
                socketio.emit('sb', 'Logged in!')
            else:
                socketio.emit('sb', 'Password incorrect')
        else:
            socketio.emit('sb', 'User not found')
    else:
        socketio.emit('sb', 'Please reload the page and try again')


@socketio.on('add user')
def add_user(json):
    if validate_csrf(json['json']['csrf']):
        socketio.emit('add user response')
        if User.get(email=json['json']['email']) is None:
            User.create(email=json['json']['email'], password=bcrypt.generate_password_hash(json['json']['password']))
            socketio.emit('sb', 'Added ' + json['json']['email'] + '!')
        else:
            socketio.emit('sb', 'Email already registered')
    else:
        socketio.emit('sb', 'Please reload the page and try again')


@app.route("/settings")
@login_required
def settings():
    pass