import os
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])
db = SQLAlchemy(app)

from models import *


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/add_post", methods=["POST"])
def form():
    return render_template("form.html")


@app.route("/<name>")
def hello_name(name):
    return "Hello {0}!".format(name)

if __name__ == "__main__":
    app.run()
