from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from qlerner.main.database import db

class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    hint = db.Column(db.String(100))
    tags = db.Column(db.String)  # comma-separated list of tags
    lessons = db.relationship('Lesson', secondary='exercises_for_lesson')
    users = db.relationship('User', secondary='user_completed_exercises', back_populates='completed_exercises')

class UserCompletedExercise(db.Model):
    __tablename__ = 'user_completed_exercises'

    user_id = db.Column(db.Integer, ForeignKey('users.id'), primary_key=True)
    exercise_id = db.Column(db.Integer, ForeignKey('exercises.id'), primary_key=True)

    user = relationship('User', back_populates='completed_exercises')
    exercise = relationship('Exercise', back_populates='users')
