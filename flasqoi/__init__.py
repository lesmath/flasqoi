from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SECRET_KEY']='!123SmileNow!'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/flasqoi.db'

db = SQLAlchemy(app)
from flasqoi import routes