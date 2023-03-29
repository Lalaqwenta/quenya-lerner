from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase
from qlerner.main.database import db

class Base(DeclarativeBase):
    pass

class Tags(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(20))


lesson_tags = Table(
    'lesson_tags',
    Base.metadata,
    db.Column("lesson_id", ForeignKey('lessons.id')),
    db.Column("tag_id", ForeignKey('tags.id')),
)

user_tags = Table(
    'user_tags',
    Base.metadata,
    db.Column("user_id", ForeignKey('users.id')),
    db.Column("tag_id", ForeignKey('tags.id')),
)

exercise_tags = Table(
    'exercise_tags',
    Base.metadata,
    db.Column("exercise_id", ForeignKey('exercises.id')),
    db.Column("tag_id", ForeignKey('tags.id')),
)


word_tags = Table(
    'word_tags',
    Base.metadata,
    db.Column("word_id", ForeignKey('words.id')),
    db.Column("tag_id", ForeignKey('tags.id')),
)