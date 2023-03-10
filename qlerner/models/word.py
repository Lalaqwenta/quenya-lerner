from qlerner.main.database import db

class Word(db.Model):
    __tablename__ = 'words'
    
    id = db.Column(db.Integer, primary_key=True)
    english_meaning = db.Column(db.String(256), nullable=False)
    english_translation = db.Column(db.String(256), nullable=False)
    quenya_tengwar = db.Column(db.String(256), nullable=False)
    quenya_transcription = db.Column(db.String(256), nullable=False)
