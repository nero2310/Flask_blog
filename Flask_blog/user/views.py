from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import bcrypt

from Flask_blog.database.db import Mongo
from Flask_blog.user.forms import UserRegisterForm, UserLoginForm

user = Blueprint("user", __name__)

database = Mongo(database="test",collection="user")


def create_hash(password: str):
    """
    Create password hash using bcrypt
    :param password:
    :return: password hash
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(rounds=14)).decode("utf-8")


@user.route("/register", methods=["GET", "POST"])
def signup():
    form = UserRegisterForm(request.form)
    if form.validate() and request.method == "POST":
        user = {
            "username": form.username.data,
            "password_hash": create_hash(form.password.data)
        }
        if database.find(data_filter={"username": form.username.data}) is None:
            print(database.find({"username": form.username.data}))
            database.insert(user)
            flash(message=f"Your account has been registered {form.username.data}")
            return redirect(url_for("user.signup_sucess", _method="GET"))
        else:
            flash(message="An account with this nickname already exists")
            return redirect(url_for("user.signup_sucess", _method="GET"))
    return render_template("auth/signup_form.html", form=form)


@user.route("/login", methods=["GET", "POST"])
def log_in():
    form = UserLoginForm(request.form)
    if form.validate() and request.method == "POST":
        form_data = {
            "username": form.username.data,
            "password": form.password.data,
        }
        user_password_hash = database.find(data_filter={"username": form_data["username"]},
                                           projection={"password_hash": 1, "_id": 0})
        if isinstance(user_password_hash, dict):
            user_password_hash = user_password_hash["password_hash"]
            if bcrypt.checkpw(password=form_data["password"].encode("utf-8"),
                              hashed_password=user_password_hash.encode("utf-8")):
                user_data = database.find(how_many="one", data_filter={"username": form_data["username"]},
                                          projection={"username": 1})
                session["username"] = user_data["username"]
                return redirect(url_for("main_page"))
    return render_template("auth/log_in_form.html", form=form)


@user.route("/sucess", methods=["GET"])
def signup_sucess():
    return render_template("auth/sucess.html")
