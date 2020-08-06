from flask import Blueprint, render_template, request, redirect, url_for, flash

from Flask_blog.database.db import Mongo
from Flask_blog.user.forms import UserRegisterForm

user = Blueprint("user", __name__)

database = Mongo()


@user.route("/user", methods=["GET", "POST"])
def signup():
    form = UserRegisterForm(request.form)
    if form.validate() and request.method == "POST":
        user = {
            "username": form.username.data,
            "email": form.email.data,
            "password": form.password.data,
        }
        database.insert(user)
        flash(message="Your account has been registered")
        return redirect(url_for("user.signup_sucess", _method="GET"))
    return render_template("auth/login_form.html", form=form)

@user.route("/sucess",methods=["GET"])
def signup_sucess():
    return render_template("auth/sucess.html")
    
