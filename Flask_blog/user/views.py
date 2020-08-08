from flask import Blueprint, render_template, request, redirect, url_for, flash
import bcrypt

from Flask_blog.database.db import Mongo
from Flask_blog.user.forms import UserRegisterForm

user = Blueprint("user", __name__)

database = Mongo()


def create_hash(password):
    return str(bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt(rounds=14)))


@user.route("/register", methods=["GET", "POST"])
def signup():
    form = UserRegisterForm(request.form)
    if form.validate() and request.method == "POST":
        user = {
            "username": form.username.data,
            "email": form.email.data,
            "password_hash": create_hash(form.password.data)
        }
        database.insert(user)
        flash(message=f"Your account has been registered {form.username.data}")
        return redirect(url_for("user.signup_sucess", _method="GET"))
    return render_template("auth/login_form.html", form=form)


@user.route("/login",methods=["GET","POST"])
# def log_in():
#     # form =

@user.route("/sucess",methods=["GET"])
def signup_sucess():
    return render_template("auth/sucess.html")
    
