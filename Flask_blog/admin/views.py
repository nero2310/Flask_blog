from flask import Blueprint, render_template

from Flask_blog.database.db import Mongo

admin_page = Blueprint("admin", __name__)


@admin_page.route("/login")
def admin_login():
    database = Mongo(database="test", collection="user", ServerSelectionTimeoutMS=5000)
    return render_template("admin/admin_login.html")
