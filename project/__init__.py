from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:polmog9439@localhost/learn-auth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'kkbh7y7hb'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from project.users.views import users_blueprint

app.register_blueprint(users_blueprint, url_prefix='/users')