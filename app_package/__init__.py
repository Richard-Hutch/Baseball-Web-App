from flask_bcrypt import Bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from myConfig import Config
from csi3335fall2021 import user


app = Flask(__name__)

# create a new database in terminal called baseballAPP
engineUrl = 'mysql+pymysql://' + user['username'] + ':' + user['password'] + '@' + user['host'] + ':3306/' + user['db']
app.config['SQLALCHEMY_DATABASE_URI'] = engineUrl
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(Config)

engine = create_engine(engineUrl)

if not database_exists(engine.url):
    create_database(engine.url)

db = SQLAlchemy(app)
# Package used to encrypt passwords for security purposes
bcrypt = Bcrypt(app)

from app_package import routes #NEEDS TO BE HERE IN THIS ORDER

# Create all the tables
db.create_all()