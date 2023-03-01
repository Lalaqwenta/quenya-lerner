from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from qlerner.main.database import db

class Lesson(db.Model):
    __tablename__ = 'lessons'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    tags = db.Column(db.String)  # comma-separated list of tags
    exercises = db.relationship('Exercise', secondary='exercises_for_lesson')
    completed_by = db.relationship('User', secondary='user_completed_lessons')

class UserCompletedLesson(db.Model):
    __tablename__ = 'user_completed_lessons'    

    user_id = db.Column(db.Integer, ForeignKey('users.id'), primary_key=True)
    lesson_id = db.Column(db.Integer, ForeignKey('lessons.id'), primary_key=True)
    completed_at = db.Column(db.DateTime)  # Unix timestamp

    user = db.relationship('User', back_populates='completed_lessons')
    lesson = db.relationship('Lesson', back_populates='completed_by')

class ExercisesForLesson(db.Model):
    __tablename__ = 'exercises_for_lesson'

    exercise_id = db.Column(db.Integer, ForeignKey('exercises.id'), primary_key=True)
    lesson_id = db.Column(db.Integer, ForeignKey('lessons.id'), primary_key=True)

    exercise = db.relationship('Exercise', back_populates='lessons')
    lesson = db.relationship('Lesson', back_populates='exercises')