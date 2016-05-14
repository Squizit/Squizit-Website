from flask.ext.wtf import RecaptchaField, Recaptcha
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired


class MemberLogin(Form):
    username = StringField(u'Username', [DataRequired()])
    password = PasswordField(u'Password', [DataRequired()])
    # recaptcha = RecaptchaField(u'Recaptcha', [Recaptcha()])
