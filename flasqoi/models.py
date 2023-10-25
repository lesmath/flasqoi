# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flasqoi import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False, unique = True)
    image_file = db.Column(db.String(20), nullable = False, default='default.jpg') 
    password = db.Column(db.String(20), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return f'{self.username}:{self.email}:{self.date_created}'
