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
    
# class Teachers(db.Model, UserMixin):

#     #setting up the database for the teachers
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Colum(db.String(150), unique=True)
#     first_name = db.Column(db.String(150))
#     last_name = db.Column(db.String(150))
#     teaching_school = db.Colmn(db.String(200))
#     teaching_style = db.Column(db.String(200))
#     teaching_subjects = db.Column(db.String(500))
#     first_language = db.Column(db.String(300))


# class Notes(db.Model, UserMixin):
#     pass
