from flask import Blueprint, request, flash, redirect, url_for, abort
from flask import render_template
from flask_login import login_user, current_user, logout_user, login_required
from qlerner.models.user import *
from qlerner.models.exercise import *
from qlerner.models.lesson import *
from qlerner.models.word import *
from qlerner.forms.login import LoginForm
from qlerner.forms.signin import SignupForm
from qlerner.main.database import db
from sqlalchemy import text
from random import sample
from functools import wraps

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/home')
def home():
    return render_template('index.html')

@routes.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data

        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('routes.signup'))

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists', 'danger')
            return redirect(url_for('routes.signup'))

        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash('Email already exists', 'danger')
            return redirect(url_for('routes.signup'))

        new_user = User(username=username, password=password, 
            email=email)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully!', 'success')
        return redirect(url_for('routes.login'))
    else:
        for err_field in form.errors:
            flash(form.errors[err_field])

    return render_template('signup.html', form=form)
   

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
    else:
        for err_field in form.errors:
            flash(form.errors[err_field])

    return render_template('login.html', form=form)

@routes.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('routes.login'))

@routes.route('/profile')
@login_required
def profile():
    user = current_user
    
    query = text("SELECT * FROM {table} WHERE user_id = '{user_id}'"
        .format(
        table=user_completed_lessons_NAMETAG, user_id=user.id
    ))
    solved_lessons = len(db.engine.connect().execute(query).fetchall())
    return render_template('profile.html', user=user, 
        solved_lessons=solved_lessons)

@routes.route('/choose_lesson', methods=['GET'])
@login_required
def choose_lesson():
    lessons = Lesson.query.all()
    return render_template('choose_lesson.html', lessons=lessons)

def return_options(exercise) -> list:
    if exercise.type == "choose one":
        all_words = Word.query.all()
        # remove the correct answer from the list of words
        words_without_answer = [word.quenya_tengwar for word 
            in all_words if word.quenya_tengwar != exercise.answer]
        # randomly select three wrong options from the remaining words
        wrong_options = sample(words_without_answer, 3)
        # combine the correct answer and the wrong options
        # shuffle the list
        return sample([exercise.answer] + wrong_options, k=4)
    return []

@routes.route('/solve_lesson/<int:lesson_id>', methods=['GET', 'POST'])
@login_required
def solve_lesson(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id)
    exercise_ids = lesson.exercise_ids.split(',')
    current_index = int(request.args.get('current_index', 0))
    current_exercise_id = int(exercise_ids[current_index])
    current_exercise = Exercise.query.get(current_exercise_id)
    current_exercise.options = return_options(current_exercise)
    if request.method == 'POST':
        # Check if answer is correct
        user_answer = request.form['answer']
        # TODO: that lower() WILL cause problems in future
        if user_answer.strip().lower() == current_exercise.answer.lower():
            # Update completed exercises for user
            user_completed_exercise = UserCompletedExercise.query.filter_by(
                user_id=current_user.id, 
                exercise_id=current_exercise.id).first()
            if user_completed_exercise:
                user_completed_exercise.times_completed += 1
            else:
                user_completed_exercise = UserCompletedExercise(
                    user_id=current_user.id, 
                    exercise_id=current_exercise.id, 
                    times_completed = 1)
                db.session.add(user_completed_exercise)
            db.session.commit()

            # Move on to next exercise or complete lesson
            if current_index == len(exercise_ids) - 1:
                # Mark lesson as completed
                user_completed_lesson = UserCompletedLesson.query.filter_by(
                    user_id=current_user.id, 
                    lesson_id=lesson.id).first()
                if user_completed_lesson:
                    user_completed_lesson.times_completed += 1
                    # user_completed_lesson.completed_at = datetime.now()
                else:
                    user_completed_lesson = UserCompletedLesson(
                        user_id=current_user.id, 
                        lesson_id=lesson.id, times_completed = 1)
                    db.session.add(user_completed_lesson)
                db.session.commit()

                flash('Congratulations, you have completed the lesson!',
                    'success')
                return redirect(url_for('routes.choose_lesson'))

            next_index = current_index + 1
            next_exercise_id = int(exercise_ids[next_index])
            next_exercise = Exercise.query.get(next_exercise_id)
            next_exercise.options = return_options(next_exercise)
            return render_template('solve_lesson.html', 
                lesson=lesson, exercise=next_exercise, 
                current_index=next_index)

        else:
            flash('Incorrect answer, please try again', 'danger')
    
    return render_template('solve_lesson.html', lesson=lesson, 
        exercise=current_exercise, current_index=current_index)

@routes.route('/words')
def words():
    words = Word.query.all()
    return render_template('words.html', words=words)

def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            flash('You need to be an admin to access this page', 
                'warning')
            return redirect(url_for('routes.home'))
        return func(*args, **kwargs)
    return decorated_view

@routes.route('/admin/create_exercise', methods=['GET', 'POST'])
@login_required
def create_exercise():
    if current_user.role != "admin":
        return abort(403)

    # handle form submission
    if request.method == 'POST':
        question = request.form['question']
        answer = request.form['answer']
        hint = request.form['hint']

        # validate form data
        if not question or not answer:
            flash('Please enter both a question and an answer', 
                'danger')
            return redirect(url_for('routes.create_exercise'))

        # create a new exercise and add it to the database
        new_exercise = Exercise(question=question, answer=answer, 
            hint=hint)
        db.session.add(new_exercise)
        db.session.commit()

        flash('Exercise created successfully', 'success')
        return redirect(url_for('routes.create_exercise'))

    # render the exercise creation form
    return render_template('create_exercise.html')