from flask import Flask, render_template, request

from . import db

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home/index.html")


@app.route("/posts/")
def posts():
    posts = db.get_posts()
    return render_template("posts/index.html", posts=posts)


@app.route("/post/<string:post_id>")
def post_view(post_id):
    post = db.get_post(post_id)
    return render_template("posts/_partials/_post.html", post=post)

@app.route("/post/delete/<string:post_id>", methods=["DELETE"])
def post_delete(post_id):
    if request.method == "DELETE":
        db.delete_post(post_id)
        return ""


@app.route("/posts/edit/<string:post_id>", methods=["GET", "PUT"])
def post_edit(post_id):
    if request.method == "PUT":
        title = request.form.get("title")
        content = request.form.get("content")
        db.update_post(post_id, title, content)
        return post_view(post_id)
    post = db.get_post(post_id)
    return render_template("posts/_partials/_edit.html", post=post)
