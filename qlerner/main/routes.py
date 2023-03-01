from flask import Blueprint, request, flash, redirect, url_for
from flask import render_template
from flask_login import login_user, current_user, logout_user, login_required
from qlerner.models.user import *
from qlerner.models.exercise import *
from qlerner.models.lesson import *
from qlerner.models.word import *
from qlerner.forms.login import LoginForm
from qlerner.forms.signin import SignIn
from qlerner.main.database import db
from sqlalchemy import text

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/home')
def home():
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

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('routes.home'))
        else:
            flash('Invalid email or password', 'danger')

    return render_template('login.html', form=form)

@routes.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('routes.login'))

@routes.route('/profile')
@login_required
def profile():
    user = current_user
    query = text("SELECT * FROM {table} WHERE user_id = '{user_id}'".format(
        table=user_completed_lessons_NAMETAG, user_id=user.id
    ))
    solved_lessons = len(db.engine.connect().execute(query).fetchall())
    return render_template('profile.html', user=user, solved_lessons=solved_lessons)

@routes.route('/choose_lesson', methods=['GET'])
@login_required
def choose_lesson():
    lessons = Lesson.query.all()
    return render_template('choose_lesson.html', lessons=lessons)

@routes.route('/solve_lesson/<int:lesson_id>', methods=['GET', 'POST'])
@login_required
def solve_lesson(lesson_id):
    exercise = Exercise.query.get(lesson_id)
    form = LessonForm()
    if form.validate_on_submit():
        if form.answer.data == exercise.answer:
            # update user's solved exercises
            current_user.solved_exercises.append(exercise)
            db.session.commit()
            flash('Congratulations! You solved the exercise!', 'success')
            return redirect(url_for('routes.choose_exercise'))
        else:
            flash('Incorrect answer. Please try again.', 'danger')
    return render_template('solve_exercise.html', form=form, exercise=exercise)
