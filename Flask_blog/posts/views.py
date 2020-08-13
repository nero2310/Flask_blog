from flask import Blueprint, render_template, request, session, flash

from Flask_blog.database.db import Mongo
from Flask_blog.posts import forms

posts = Blueprint("posts", __name__)

database = Mongo(database="test", collection="posts")


@posts.route("/create", methods=["GET", "POST"])
def create_post():
    form = forms.CreatePostForm(request.form)
    if form.validate() and request.method == "POST":
        if not "username" in session:
            flash("You have to be logged in to add a post")
        else:
            post = {
                "title": form.title.data,
                "content": form.content.data,
                "approved": False,
                "author": session["username"]
            }
            database.insert(post)
            flash("Post was created")
    return render_template("posts/create_post_form.html", form=form)


@posts.route("/", methods=["GET", "POST"])
def list_post():
    all_post = database.find(how_many="all", data_filter={"approved": True},
                             projection={"content": 1, "title": 1, "author": 1})
    return render_template("posts/show_posts.html", posts=all_post)
