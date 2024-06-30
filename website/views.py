from flask import Blueprint, render_template
views = Blueprint("views", __name__)


# student and teacher login page
@views.route("/")
def role_select():
    return render_template("opening_page.html")

# Page to select what type of learner the student is
@views.route("/learner_type")
def learner_type():
    return render_template("learner_type.html")



# subject selection page
@views.route("/subjects")
def subjects():
    return render_template("subjects_page.html")


