from flask import Flask, render_template

from . import db

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home/index.html")


@app.route("/posts/")
def posts():
    posts = db.get_posts()
    return render_template("posts/index.html", posts=posts)
