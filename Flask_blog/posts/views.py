from flask import Blueprint, render_template, request, session, flash
from pymongo.errors import DuplicateKeyError

from Flask_blog.database.db import Mongo
from Flask_blog.posts import forms

posts = Blueprint("posts", __name__)


@posts.route("/create", methods=["GET", "POST"])
def create_post():
    database = Mongo(database="test", collection="posts", ServerSelectionTimeoutMS=5000)
    form = forms.CreatePostForm(request.form)
    if form.validate() and request.method == "POST":
        if not "username" in session:
            flash("You have to be logged in to add a post")
        else:
            post = {
                "title": form.title.data,
                "content": form.content.data,
                "description": form.description.data,
                "approved": False,
                "xss_protection_disabled": False,
                "author": session["username"]
            }
            try:
                database.insert(post)
                flash("Post was created")
                flash("Admin soon will check your post")
            except DuplicateKeyError:
                flash("This post title exist")
    return render_template("posts/create_post_form.html", form=form)


@posts.route("/<title>")
def get_post(title):
    database = Mongo(database="test", collection="posts", ServerSelectionTimeoutMS=5000)
    post = database.find(how_many="one", data_filter={"approved": True, "title": title},
                         projection={"content": 1, "author": 1, "title": 1, "xss_protection_disabled": 1})
    database = Mongo(database="test", collection="user", ServerSelectionTimeoutMS=5000)
    author = database.find(how_many="one", data_filter={"username": post["author"]}, projection={"trusted_user": 1})
    return render_template("posts/render_post.html", post=post, author=author)


@posts.route("/", methods=["GET", "POST"])
def list_post():
    database = Mongo(database="test", collection="posts", ServerSelectionTimeoutMS=5000)
    all_post = database.find(how_many="all", data_filter={"approved": True},
                             projection={"content": 1, "title": 1, "description": 1, "author": 1})
    return render_template("posts/show_posts.html", posts=all_post)
