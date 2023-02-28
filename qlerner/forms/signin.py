from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp

class SignIn(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),
            Email(), Length(max=120)])
    password = PasswordField('Password', validators=[Length(max=60)])
    username = StringField('Username', validators=[DataRequired(), 
            Regexp(regex="[A-Z][A-z]+"), Length(max=120)])
