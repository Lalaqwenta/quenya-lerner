from flask import Flask
from qlerner.main.routes import *
from qlerner.main.database import *

app = Flask(__name__)
app.register_blueprint(routes)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quenya-lerner.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
