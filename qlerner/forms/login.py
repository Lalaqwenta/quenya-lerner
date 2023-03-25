from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    login_data = StringField('Email or Username', validators=[DataRequired(), 
        Length(max=120)])
    password = StringField('Password', validators=[DataRequired(), 
        Length(min=8, max=60)])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log in')
