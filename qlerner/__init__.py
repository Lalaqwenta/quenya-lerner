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

application = Flask(__name__)
application.register_blueprint(routes)
application.register_blueprint(exercise_routes)
application.register_blueprint(user_routes)
application.register_blueprint(lesson_routes)
application.register_blueprint(word_routes)
application.config.from_object(Config)
application.jinja_env.filters['tw'] = tengwarize

application.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'
application.config['LANGUAGES'] = {
    'en': 'English',
    'ru': 'Russian'
}

babel = Babel(application, default_locale='ru', default_timezone='GMT+3', locale_selector=locale_select)

lm.init_app(application)
lm.login_view = 'login'
init_app(application)

@application.route("/")
def hello():
   return "<h1 style='color:blue'>Hello There!</h1>"

if __name__ == '__main__':
    application.run(host='0.0.0.0')
