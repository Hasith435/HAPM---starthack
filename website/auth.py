from flask import Blueprint, render_template, flash, redirect, request, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)

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

        user = User.query.filter_by(email=email).first()

        if user:
            print('already there')
            flash('Email already exists', category='error')
        else:
            print('registered')
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password, method='scrypt'), last_name=last_name, school=school, address=address, city=city, zip=zip)
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!', category='success')

            login_user(new_user, remember=True)

            return redirect(url_for('views.learner_type'))

    return render_template("Signin.html")

@auth.route("/login", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        print('post request login')
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

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