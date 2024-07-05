from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Association table for the many-to-many relationship between students and notes
students_notes = db.Table('students_notes',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
    db.Column('note_id', db.Integer, db.ForeignKey('note.note_id'), primary_key=True)  # Corrected foreign key reference
)

class Student(db.Model, UserMixin):
    # Setting up the user database for login and sign up
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    school = db.Column(db.String(300), nullable=True)
    address = db.Column(db.String(1000), nullable=True)
    city = db.Column(db.String(1000), nullable=True)
    zip = db.Column(db.String(1000), nullable=True)
    password = db.Column(db.String(150), nullable=False)
    notes = db.relationship('Note', secondary=students_notes, backref=db.backref('students', lazy=True))

class Note(db.Model):
    # Setting up the notes table
    note_id = db.Column(db.Integer, primary_key=True)
    note_title = db.Column(db.String(150), nullable=False)
    learning_type = db.Column(db.String(200), nullable=True)
    language = db.Column(db.String(200), nullable=True)
    note_content = db.Column(db.Text, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)

class Teacher(db.Model, UserMixin):
    # Setting up the database for the teachers
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    teaching_school = db.Column(db.String(200), nullable=True)  # Fixed typo here
    teaching_style = db.Column(db.String(200), nullable=True)
    teaching_subjects = db.Column(db.String(500), nullable=True)
    first_language = db.Column(db.String(300), nullable=True)

    notes = db.relationship('Note', backref='teacher', lazy=True)
