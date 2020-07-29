from flask import Blueprint, render_template, request, flash
from Flask_blog.user.forms import UserRegisterForm
from Flask_blog.user.models import UserModel

user = Blueprint("user", __name__)


@user.route("/user", methods=["GET","POST"])
def signup():
    form = UserRegisterForm(request.form)
    if request.method =="POST" and form.validate():
        user = UserModel(form.username,"dummy_data@wp.pl",form.password)
        flash(f"Thanks for register {form.username}")
    return render_template("auth/login_form.html", form=UserRegisterForm())
