from flask import Flask, request
from flask_bootstrap import Bootstrap
from flask_babel import Babel

app = Flask(__name__)

app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['LANGUAGES'] = ['en', 'uk', 'pseudo', 'ids']

bootstrap = Bootstrap(app)
babel = Babel(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


from app import routes
