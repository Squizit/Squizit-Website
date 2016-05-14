from flask import render_template
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


@socketio.on('login user')
def user_form(json):
    if validate_csrf(json['json']['csrf']):
        socketio.emit('sb', 'CSRF Verified Successfully')
    else:
        socketio.emit('sb', 'CSRF did not verify')


@socketio.on('add user')
def add_user(json):
    if validate_csrf(json['json']['csrf']):
        if User.get(email=json['json']['email']) is None:
            User.create(email=json['json']['email'], password=bcrypt.generate_password_hash(json['json']['email']))
            socketio.emit('sb', 'Added ' + json['json']['email'] + '!')
        else:
            socketio.emit('sb', 'Email already registered')
    else:
        socketio.emit('sb', 'Please reload the page and try again')