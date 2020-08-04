from os import environ

from flask import Flask, render_template
from flask_login import LoginManager

from Flask_blog.user.views import user
from Flask_blog.config_loader import load_environment_variables

load_environment_variables(".env")
app = Flask(__name__)
app.register_blueprint(user, url_prefix="/auth")
try:
    app.config["SECRET_KEY"] = environ["secret_key"]
    login_manager = LoginManager()
    login_manager.init_app(app)
except KeyError:
    print("Your config file doesn't contain secret key")
    exit(0)


@app.route("/")
def hello_word():
    return render_template("site/base_bootstrap.html")


@app.route("/login")
def login_page():
    return render_template("auth/login_form.html")


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


if __name__ == "__main__":
    if environ["env"] == "development":
        app.run(debug=True)
    elif environ["env"] == "production":
        app.run(debug=False)
