from flask import Blueprint, render_template, session
from . import db
from firebase_admin import  auth as firebase_auth
views = Blueprint("views", __name__)


# student and teacher login page
@views.route("/")
def role_select():
    return render_template("opening_page.html")


# STUDENT PAGES
# Page to select what type of learner the student is
@views.route("/learner_type")
def learner_type():
    return render_template("learner_type.html")

# subject selection page
@views.route("/subjects")
def subjects():

    current_logged_in_user_email = session['user']
    decoded_token = firebase_auth.verify_id_token(session['id_token'])
    user_id = decoded_token['uid']
    print(f"currently logged in user_id: {user_id}")
    user_details = db.collection('users').document(user_id).get().to_dict()
    
    user_first_name = user_details['first_name']


    return render_template("subjects_page.html", user_first_name = user_first_name)


@views.route("/comp_sci")
def comp_sci():
    return render_template("comp_sci_page.html")

@views.route("/chemistry")
def chemistry():
    return render_template("chemistry_index.html")


@views.route("/user_display")
def user_display():

    users_ref = db.collection('users')
    docs = users_ref.stream()
    users = [{'id':doc.id, 'email':doc.to_dict()['email'],'first_name': doc.to_dict()['first_name'], 'last_name':doc.to_dict()['last_name'], 'school':doc.to_dict()['school']} for doc in docs]


    return render_template("user_display.html", users = users)



#TEACHER PAGES

@views.route("/subjects_teachers")
def subjects_teachers():
    return render_template("subjects_page_teachers.html", subjects=["Chemistry, Physics, Maths"])

@views.route("/comp_sci_teachers")
def comp_sci_teachers():
    return render_template("comp_sci_page.html")