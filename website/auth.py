from flask import Blueprint, render_template, flash, redirect, request, url_for, session
from . import db
import pyrebase

auth = Blueprint("auth", __name__)

config = {
        'apiKey': "AIzaSyBDCmYDAF7UkA2l0WxKuvd8kQ298iZrHLw",
    'authDomain': "brew-crew-7690e.firebaseapp.com",
    'projectId': "brew-crew-7690e",
    'storageBucket': "brew-crew-7690e.appspot.com",
    'messagingSenderId': "1039714422898",
    'appId': "1:1039714422898:web:979b5d71e4893653ac72eb",
    'databaseURL' : ''
        }

firebase = pyrebase.initialize_app(config)
auth_firebase = firebase.auth()

# AUTHENTICATION FOR STUDENTS
@auth.route("/login", methods=['POST', 'GET'])
def login():

    if 'user' in session:
        return redirect(url_for("views.subjects"))

    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        try:
            user = auth_firebase.sign_in_with_email_and_password(email, password)
            print(user)
            session['user'] = email
            session['user_id'] = user['localId']
            session['id_token'] = user['idToken']

            return redirect(url_for("views.subjects"))
        except:
            flash("Incorrect password or username", category='error')

    return render_template("login.html")

@auth.route("/sign_up", methods=['POST', 'GET'])
def sign_up():
    
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        school = request.form.get('school')
        learning_type = request.form.get('learner-type')
        prefered_language = request.form.get('language')
        password = request.form.get('password1')
        confirm_password = request.form.get("password2")

        print(f"email: {email}")
        print(f"password: {password}")

        

        if password == confirm_password:
            user = auth_firebase.create_user_with_email_and_password(email, password)
            user_id = user['localId']
            db.collection("users").document(user_id).set({'email':email,'first_name':first_name, 'last_name':last_name, 'school':school, 'learning type':learning_type, 'prefered language': prefered_language,'client_type':'student' })
            return redirect(url_for('auth.login'))
        else:
            flash("Passwords should match", category='error')
    
    return render_template("SignIn.html")

@auth.route("/logout", methods=['GET', 'POST'])
def logout():

    session.pop('user')
    session.pop('user_id')
    session.pop('id_token')
    return redirect(url_for('views.role_select'))



# AUTHENTICATION FOR TEACHERS
@auth.route('/login_teachers', methods=['POST', 'GET'])
def login_teacher():
    if 'user' in session:
        return redirect(url_for("views.subjects"))

    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        try:
            user = auth_firebase.sign_in_with_email_and_password(email, password)
            print(user)
            session['user'] = email
            session['user_id'] = user['localId']
            session['id_token'] = user['idToken']

            return redirect(url_for("views.comp_sci_teachers"))
        except:
            flash("Incorrect password or username", category='error')

    return render_template("login_teacher.html")

@auth.route('/signup_teacher', methods=['GET', 'POST'])
def sign_up_teachers():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        school = request.form.get('school')
        teaching_method = request.form.get('learning-style')
        teaching_subject= request.form.get('teaching-subject')
        language = request.form.get('language')
        password = request.form.get('password1')
        confirm_password = request.form.get("password2")

        print(f"email: {email}")
        print(f"password: {password}")

        

        if password == confirm_password:
            user = auth_firebase.create_user_with_email_and_password(email, password)
            user_id = user['localId']
            db.collection("teachers").document(user_id).set({'email':email,'first_name':first_name, 'last_name':last_name, 'school':school, 'teaching_method':teaching_method, 'teaching_subject': teaching_subject,'language': language,'client_type':'teacher' })
            return redirect(url_for('auth.login_teacher'))
        else:
            flash("Passwords should match", category='error')
    
    return render_template("signup_teachers.html")
