from flask import Blueprint, request, redirect, url_for
from flask import render_template
from qlerner.models.user import User
from qlerner.models.exercise import Exercise
from qlerner.models.word import Word
from qlerner.main.database import db

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            return render_template('signup.html', error='Passwords do not match')

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return render_template('signup.html', error='Email already exists')

        new_user = User(username=username, password=password, email=email)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('routes.login'))

    return render_template('signup.html')    

@routes.route('/login')
def login():
    return "Not done yet"