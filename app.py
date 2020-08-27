from os import environ

from flask import Flask, render_template
from pymongo.errors import ServerSelectionTimeoutError

from Flask_blog.user.views import user
from Flask_blog.posts.views import posts
from Flask_blog.admin.views import admin_page
from Flask_blog.config_loader import load_environment_variables

load_environment_variables(".env")


def create_app():
    app = Flask(__name__)
    try:
        app.config["SECRET_KEY"] = environ["secret_key"]
    except KeyError:
        print("Your config file doesn't contain secret key")
        exit(0)

    @app.route("/")
    def main_page():
        return render_template("site/base.html")

    app.register_blueprint(user, url_prefix="/auth")
    app.register_blueprint(posts, url_prefix="/posts")
    app.register_blueprint(admin_page, url_prefix="/admin")
    @app.errorhandler(ServerSelectionTimeoutError)
    def database_timeout(e):
        return render_template("errors/database_timeout.html")

    return app


if __name__ == "__main__":
    if environ["env"] == "development":
        app = create_app()
        app.run(debug=True, host="0.0.0.0")
    elif environ["env"] == "production":
        app = create_app()
        app.run(debug=False, host="0.0.0.0")

