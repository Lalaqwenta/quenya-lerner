import os

class Config:
    DATABASE = os.environ.get('DATABASE') or \
        os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'quenya.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        "sqlite:///" + DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///quenya-lerner.db'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
