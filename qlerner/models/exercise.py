from qlerner.main.database import db

class Exercise(db.Model):
    __tablename__ = 'exercises'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.String(200), nullable=False)
    hint = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    completed_by = db.relationship('User', secondary='completed_exercises')

completed_exercises = db.Table('completed_exercises',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercises.id'))
)
