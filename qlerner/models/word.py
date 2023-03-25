from qlerner.main.database import db

class Word(db.Model):
    __tablename__ = 'words'
    
    id = db.Column(db.Integer, primary_key=True)
    english_meaning = db.Column(db.String(256), nullable=False)
    english_translation = db.Column(db.String(256), nullable=False)
    quenya_tengwar = db.Column(db.String(256), nullable=False)
    quenya_transcription = db.Column(db.String(256), nullable=False)

    def clone(self):
        d = dict(self.__dict__)
        d.pop("id")
        d.pop("_sa_instance_state")
        copy = self.__class__(**d)
        db.session.add(copy)
        db.session.commit()
        return copy
