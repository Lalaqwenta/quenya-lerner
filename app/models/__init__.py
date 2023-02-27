from app import db

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    english = db.Column(db.String(64), index=True, unique=True)
    quenya = db.Column(db.String(64), index=True, unique=True)
    image_url = db.Column(db.String(128))

    def __repr__(self):
        return f'<Word {self.english} ({self.quenya})>'
