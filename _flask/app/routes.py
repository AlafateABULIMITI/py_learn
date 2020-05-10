from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Felix"}
    posts = [
        {"author": {"username": "John"}, "body": "Beautiful day in Portland!"},
        {"author": {"username": "Susan"}, "body": "The Avengers movie was so cool!"},
    ]
    """
    The `render_template()` function calls the Jinja2 template engine that the Flask framework natively depends on. Jinja2 replaces `{{...}}` with the corresponding value in the incoming argument of the `render_template()` function block.
    """
    return render_template("index.html", title="Home", user=user, posts=posts)
