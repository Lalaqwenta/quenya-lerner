from flask import Flask
from flask_migrate import Migrate
from qlerner.main.routes import *
from qlerner.database.db import *
from qlerner.config import Config

app = Flask(__name__)
app.register_blueprint(routes)
app.config.from_object(Config)

init_app(app)

if __name__ == '__main__':
    # migrate = Migrate(app=app, db=db)
    app.run(debug=True)
