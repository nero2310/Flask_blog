from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import bcrypt
from werkzeug.utils import redirect

from Flask_blog.database.db import Mongo
from Flask_blog.user.forms import UserRegisterForm, UserLoginForm

user = Blueprint("user", __name__)

# database = Mongo(database="test", collection="user", ServerSelectionTimeoutMS=5000)


def create_hash(password: str):
    """
    Create password hash using bcrypt
    :param password:
    :return: password hash
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(rounds=14)).decode("utf-8")


@user.route("/register", methods=["GET", "POST"])
def signup():
    database = Mongo(database="test", collection="user", ServerSelectionTimeoutMS=5000)
    form = UserRegisterForm(request.form)
    if form.validate() and request.method == "POST":
        user = {
            "username": form.username.data,
            "password_hash": create_hash(form.password.data),
            "trusted_user": False,  # trusted_user posts will not be protected from xss attack
            "is_admin": False  # this have to be a bool don't use it like string "False" boolean value is true !!!
        }
        if database.find(data_filter={"username": form.username.data}) is None:
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
        if password_checker(form.username.data, form.password.data):
            session["username"] = form.username.data
            return redirect(url_for("main_page"))
    return render_template("auth/log_in_form.html", form=form)


@user.route("/sucess", methods=["GET"])
def signup_sucess():
    return render_template("auth/sucess.html")


@user.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("main_page"))


def password_checker(username, password) -> bool:
    """
    Chceck if password is equal to user password
    :param username:check password for this user
    :param password:
    :return:
    True if password match, False otherwise
    """
    database = Mongo(database="test", collection="user", ServerSelectionTimeoutMS=5000)
    user_password_hash_db = database.find(data_filter={"username": username},
                                          projection={"password_hash": 1, "_id": 0})
    if isinstance(user_password_hash_db, dict):
        if bcrypt.checkpw(password.encode("utf-8"),
                          hashed_password=user_password_hash_db["password_hash"].encode("utf-8")):
            return True
    return False
