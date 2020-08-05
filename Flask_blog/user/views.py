from flask import Blueprint, render_template, request, flash
from Flask_blog.user.forms import UserRegisterForm
from Flask_blog.user.models import UserModel

user = Blueprint("user", __name__)


@user.route("/user", methods=["GET", "POST"])
def signup():
    form = UserRegisterForm(request.form)
    if form.validate() and request.method == "POST":
        user = UserModel(form.username, form.email, form.password).signup()
        flash(f"Thanks for register {form.username.data}")
    return render_template("auth/login_form.html", form=form)
