from flask import Flask, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_babel import Babel
from flask_mail import Mail
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

bootstrap = Bootstrap(app)
babel = Babel(app)
mail = Mail(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


from app import routes
