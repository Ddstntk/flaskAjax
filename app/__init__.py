from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask_session import Session
from werkzeug.contrib.cache import MemcachedCache

app = Flask(__name__)
app.config.from_object(Config)
print(app.config['SECRET_KEY'])
Session(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import routes