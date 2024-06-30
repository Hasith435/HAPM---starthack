from flask import Blueprint, render_template
auth = Blueprint("auth", __name__)

@auth.route("/signUp")
def sign_up():
    return render_template("Signin.html")