import os
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])
db = SQLAlchemy(app)

from models import *


@app.route("/")
def show_posts():
    latest_posts_list = Post.query.order_by(Post.date.desc()).limit(10)
    return render_template("index.html", latest_posts_list=latest_posts_list)


@app.route("/add_post", methods=["GET", "POST"])
def form():
    return render_template("form.html")


if __name__ == "__main__":
    app.run()
