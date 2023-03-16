from flask import Flask
from qlerner.main.routes import *
from qlerner.database.db import *
from qlerner.main.login_manager import lm
from qlerner.config import Config
from flask_babel import Babel

app = Flask(__name__)
app.register_blueprint(routes)
app.config.from_object(Config)

app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'
app.config['LANGUAGES'] = {
    'en': 'English',
    'ru': 'Russian'
}

babel = Babel(app, default_locale='ru', default_timezone='GMT+3', locale_selector=locale_select)

lm.init_app(app)
lm.login_view = 'login'
init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
