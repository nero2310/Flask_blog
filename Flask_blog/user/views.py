from flask import Blueprint, render_template, request
from Flask_blog.user.forms import UserRegisterForm
from Flask_blog.database.db import Mongo

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
    return render_template("auth/login_form.html", form=form)
