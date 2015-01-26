import os
from datetime import datetime
import requests
from flask import Flask, render_template, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])
db = SQLAlchemy(app)

from models import *


@app.route("/")
def show_posts():
    latest_posts_list = Post.query.order_by(Post.date.desc()).limit(10)
    return render_template("index.html", latest_posts_list=latest_posts_list)


@app.route("/submit")
def form():
    return render_template("form.html")


@app.route("/add_post", methods=["POST"])
def add_post():
    if request.method == "POST":
        # Make sure a name has been submitted
        if request.form["name"] == "":
            error_message = "You need to input a name!"
            return render_template("form.html", error_message=error_message)
        else:
            post_name = request.form["name"]

        # Make sure a comment has been submitted
        if request.form["comment"] == "":
            error_message = "You need to input a comment!"
            return render_template("form.html", error_message=error_message)
        else:
            post_comment = request.form["comment"]

        # Make sure you get a valid url
        post_website = request.form["website"]
        if post_website == "":
            pass
        elif "http://" not in post_website[:7]:
            post_website = "http://" + post_website
            try:
                url = requests.get(post_website)
            except:
                post_website = ""
                error_message = "Unable to get URL. Please make sure it's valid \
                                 and try again."
                return render_template("form.html",
                                       error_message=error_message)

        post_email = request.form["email"]
        post_date = datetime.utcnow()

        try:
            post = Post(name=post_name, comment=post_comment, email=post_email,
                        website=post_website, date=post_date
                        )
            db.session.add(post)
            db.session.commit()
        except:
            error_message = "Unable to save your post, sorry!"
            return render_template("form.html", error_message=error_message)

        return redirect(url_for("show_posts"))


if __name__ == "__main__":
    app.run()
