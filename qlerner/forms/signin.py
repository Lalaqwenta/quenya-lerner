from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), 
        Regexp(regex="([A-Z][A-z]+[ _]?)+"), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(), 
        Length(max = 120)])
    password = StringField('Password', validators=[DataRequired(), 
        Length(min=8, max=60)])
    confirm_password = StringField('Confirm Password', 
        validators=[DataRequired(), EqualTo('password', 
                message='Passwords must match')])
    submit = SubmitField('Sign Up')
