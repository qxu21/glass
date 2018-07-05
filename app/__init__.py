from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#from flask_bcrypt import Bcrypt
#from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
#migrate = Migrate(app, db)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'index' #CHANGE
#bcrypt = Bcrypt(app)

from app import views, models
