from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user
views = Blueprint("views", __name__)


# student and teacher login page
@views.route("/")
def role_select():
    return render_template("opening_page.html")

# Page to select what type of learner the student is
@views.route("/learner_type")
@login_required
def learner_type():
    return render_template("learner_type.html")



# subject selection page
@views.route("/subjects")
@login_required
def subjects():
    return render_template("subjects_page.html", username=current_user.first_name)


@views.route("/comp_sci")
@login_required
def comp_sci():
    return render_template("comp_sci_page.html", username=current_user.first_name)

@views.route("/chemistry")
@login_required
def chemistry():
    return render_template("chemistry_index.html")

