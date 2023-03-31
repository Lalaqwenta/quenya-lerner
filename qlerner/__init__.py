from flask import Flask
from qlerner.main.routes import routes, locale_select
from qlerner.main.exercise_routes import exercise_routes
from qlerner.main.user_routes import user_routes
from qlerner.main.lesson_routes import lesson_routes
from qlerner.main.word_routes import word_routes
from qlerner.database.db import *
from qlerner.main.login_manager import lm
from qlerner.config import Config
from qlerner.models.tengwarize import tengwarize
from flask_babel import Babel

app = Flask(__name__)
app.register_blueprint(routes)
app.register_blueprint(exercise_routes)
app.register_blueprint(user_routes)
app.register_blueprint(lesson_routes)
app.register_blueprint(word_routes)
app.config.from_object(Config)
app.jinja_env.filters['tw'] = tengwarize

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
