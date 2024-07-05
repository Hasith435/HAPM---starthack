from flask import Blueprint, render_template, flash, redirect, request, url_for
from .models import Student, Teacher, Note
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)

# these are the auth function for students
@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("views.role_select"))

@auth.route("/signUp", methods=['GET', 'POST'])
def sign_up():

    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password1')
        confirm_password = request.form.get('password2')
        school = request.form.get('school')
        address = request.form.get('address')
        city = request.form.get('city')
        zip = request.form.get('zip')


        user = Student.query.filter_by(email=email).first()

        if confirm_password == password:
            if user:
                print('already there')
                flash('Email already exists', category='error')
            else:
                print('registered')
                new_user = Student(email=email, first_name=first_name, password=generate_password_hash(password, method='scrypt'), last_name=last_name, school=school, address=address, city=city, zip=zip)
                db.session.add(new_user)
                db.session.commit()
                flash('Account Created!', category='success')

                login_user(new_user, remember=True)

                return redirect(url_for('views.learner_type'))
        else:
            flash('Passwords should be the same', category='error')

    return render_template("Signin.html")

@auth.route("/login", methods=['GET', 'POST'])
def login():


    if request.method == 'POST':
        print('post request login')
        email = request.form.get('email')
        password = request.form.get('password')

        user = Student.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.subjects'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template('login.html')



# these are the auth functions for teachers
@auth.route("/logout_teacher")
def logout_teacher():
    logout_user()
    return redirect(url_for("views.role_select"))

@auth.route("/signup-teacher", methods=['GET', 'POST'])
def sign_up_teacher():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password1')
        confirm_password = request.form.get('password2')
        school = request.form.get('school')
        teaching_style = request.form.get('learning-style')
        teaching_subjects = request.form.get('teaching-subjects')
        language = request.form.get('language') 

        user = Teacher.query.filter_by(email=email).first()

        if confirm_password == password:
            if user:
                print('already there')
                flash('Email already exists', category='error')
            else:
                print('registered')
                new_user_teacher = Teacher(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(password, method='scrypt'), teaching_school=school, teaching_style=teaching_style, teaching_subjects=teaching_subjects, first_language=language)
                db.session.add(new_user_teacher)
                db.session.commit()
                flash('Account Created!', category='success')

                login_user(new_user_teacher, remember=True)

                return redirect(url_for('views.subjects_teachers'))
        else:
            flash('Passwords should be the same', category='error')

    return render_template("signup_teachers.html")


@auth.route("/login_teacher", methods=['GET', 'POST'])
def login_teacher():
    if request.method == 'POST':
        email_form = request.form.get('email')
        password = request.form.get('password')

        user_teacher = Teacher.query.filter_by(email=email_form).first()
        print(f"teacher: {user_teacher}")

        if user_teacher:
            if check_password_hash(user_teacher.password, password):
                flash('Logged in successfully', category='success')
                login_user(user_teacher, remember=True)
                return redirect(url_for('views.subjects_teachers'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template('login_teacher.html')