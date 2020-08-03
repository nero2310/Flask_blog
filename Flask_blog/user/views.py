from flask import Blueprint, render_template, request, flash
from Flask_blog.user.forms import UserRegisterForm
from Flask_blog.user.models import UserModel

user = Blueprint("user", __name__)


@user.route("/user", methods=["GET", "POST"])
def signup():
    form = UserRegisterForm()
    if form.validate_on_submit:
        user = UserModel(form.username, form.email, form.password).signup()
        flash(f"Thanks for register {form.username.data}")
    return render_template("auth/login_form.html", form=form)
