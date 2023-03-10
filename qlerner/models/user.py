from qlerner.main.database import db
from qlerner.main.login_manager import lm
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    remember_token = db.Column(db.String(128), nullable=False, default='')

    def check_password(self, _password: str) -> bool:
        return _password == self.password


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))