from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):

    # setting up the user database for login and sign up
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    school = db.Column(db.String(300))
    address = db.Column(db.String(100000))
    city = db.Column(db.String(100000))
    zip = db.Column(db.String(100000))
    password = db.Column(db.String(150))
    
