from flask import Blueprint, render_template

views = Blueprint(__name__, "views")


# student and teacher login page
@views.route("/")
def role_select():
    return render_template("opening_page.html")

# Sign in page for students and teachers
# @views.route("/sign_in")
# def home():
#     return render_template("SignIn.html")

