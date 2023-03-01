from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from qlerner.main.database import db

class Lesson(db.Model):
    __tablename__ = 'lessons'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    tags = db.Column(db.String)  # comma-separated list of tags

user_completed_lessons_NAMETAG = 'user_completed_lessons'
user_completed_lessons = db.Table(user_completed_lessons_NAMETAG,
    db.Column('user_id', db.Integer, ForeignKey('user.id'), primary_key=True),
    db.Column('lessons_id', db.Integer, ForeignKey('lessons.id'), primary_key=True),
    db.Column('completed_at', db.DateTime)
)

exercises_for_lesson_NAMETAG = 'exercises_for_lesson'
exercises_for_lesson = db.Table(exercises_for_lesson_NAMETAG,
    db.Column('exercises_id', db.Integer, ForeignKey('exercises.id'), primary_key=True),
    db.Column('lessons_id', db.Integer, ForeignKey('lessons.id'), primary_key=True)
)