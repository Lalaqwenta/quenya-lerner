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

completed_exercises_NAMETAG = 'completed_exercises'
completed_exercises = db.Table(completed_exercises_NAMETAG,
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercises.id'))
)