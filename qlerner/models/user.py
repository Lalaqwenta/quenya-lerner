from qlerner.main.database import db
from qlerner.main.login_manager import lm

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    exercises = db.relationship('Exercise', backref='user', lazy=True)
    is_active = False

    def check_password(self, _password: str) -> bool:
        return _password == self.password

@lm.user_loader
def user_loader(user):
    return User.get(user)