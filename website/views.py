from flask import Blueprint, render_template, session
from . import db
from firebase_admin import  auth as firebase_auth
from website.matcher import matcher_func
views = Blueprint("views", __name__)

current_subject = ""

# student and teacher login page
@views.route("/")
def role_select():
    return render_template("opening_page.html")


# STUDENT PAGES
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
    global current_subject 
    student_details = db.collection('users').document(session['user_id']).get().to_dict()
    current_subject = "computer_science"
    return render_template("comp_sci_page.html", username=student_details['first_name'])

@views.route("/chemistry")
def chemistry():
    global current_subject
    current_subject = "chemistry"
    return render_template("chemistry_index.html")

@views.route("/questions")
def questions():
    return render_template("questions.html")

@views.route("/recomender_page")
def recommendations():

    student_details = db.collection('users').document(session['user_id']).get().to_dict()

    student_school = student_details['school']
    student_learning_type = student_details['learning type']
    student_preferred_language = student_details['prefered language']
    student_subject = current_subject

    tutor_list = matcher_func(student_school, student_learning_type, student_preferred_language, current_subject)
    print(f"tutor list: {tutor_list}")

    return render_template("tutor_recommendations.html", tutor_list = tutor_list, student_name = student_details['first_name'])

@views.route("/enroll")
def enroll():
    student_details = db.collection('users').document(session['user_id']).get().to_dict()
    student_school = student_details['school']
    student_learning_type = student_details['learning type']
    student_preferred_language = student_details['prefered language']




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