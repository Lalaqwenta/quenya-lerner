from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from qlerner.main.database import db

completed_exercises_NAMETAG = 'completed_exercises'

class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False, default='write')
    hint = db.Column(db.String(100))
    tags = db.Column(db.String)  # comma-separated list of tags

    def clone(self):
        d = dict(self.__dict__)
        d.pop("id")
        d.pop("_sa_instance_state")
        copy = self.__class__(**d)
        db.session.add(copy)
        db.session.commit()
        return copy


class UserCompletedExercise(db.Model):
    __tablename__ = 'user_completed_exercises'

    user_id = db.Column(db.Integer, ForeignKey('users.id'), primary_key=True)
    exercise_id = db.Column(db.Integer, ForeignKey('exercises.id'), primary_key=True)
    times_completed = db.Column(db.Integer, nullable=False, default=0)
