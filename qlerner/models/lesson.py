from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from qlerner.main.database import db

user_completed_lessons_NAMETAG = 'user_completed_lessons'
exercises_for_lesson_NAMETAG = 'exercises_for_lesson'

class Lesson(db.Model):
    __tablename__ = 'lessons'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    tags = db.Column(db.String)  # comma-separated list of tags
    exercise_ids = db.Column(db.String) # comma-separated list of exercises

class UserCompletedLesson(db.Model):
    __tablename__ = 'user_completed_lessons'    

    user_id = db.Column(db.Integer, ForeignKey('users.id'), primary_key=True)
    lesson_id = db.Column(db.Integer, ForeignKey('lessons.id'), primary_key=True)
    # completed_at = db.Column(db.DateTime)  # Unix timestamp
    times_completed = db.Column(db.Integer, nullable=False, default=0)

class ExercisesForLesson(db.Model):
    __tablename__ = 'exercises_for_lesson'

    exercise_id = db.Column(db.Integer, ForeignKey('exercises.id'), primary_key=True)
    lesson_id = db.Column(db.Integer, ForeignKey('lessons.id'), primary_key=True)
