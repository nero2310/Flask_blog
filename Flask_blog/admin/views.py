from flask import Blueprint, render_template, session

from Flask_blog.database.db import Mongo

admin_page = Blueprint("admin", __name__)


@admin_page.route("/")
def admin_main():
    if session.get("username"):
        if permissions_checker(session["username"]):
            return "<h1>You are Admin</h1>"
        else:
            return "<h1>You are not a Admin</h1>"
    else:
        return "<h1>Somebody not logged in</h1>"


def permissions_checker(username) -> bool:
    """:return True if user is admin otherwise return False """
    database = Mongo(database="test", collection="user")
    is_admin = database.find(how_many="one", data_filter={"username": session["username"]}, projection={"is_admin": 1})
    if is_admin.get("is_admin"):
        return True
    return False
