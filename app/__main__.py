from flask import Flask, render_template
from flask_flatpages import pygments_style_defs

import sys

from app import app, flatpages, freezer


@app.route("/")
def homepage():
    post = flatpages.get_or_404(f"{app.config['POST_DIR']}/homepage")
    return render_template("post.html", post=post)

@app.route("/post/")
def listPosts():
    posts = [p for p in flatpages if p.path.startswith(app.config["POST_DIR"])]
    posts.sort(key=lambda item:item['date'], reverse=False)
    return render_template('postList.html', posts=posts)

@app.route('/post/<string:name>/')
def post(name):
    path = '{}/{}'.format(app.config["POST_DIR"], name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)

@app.route("/about/")
def about():
    return "Placeholder"

@app.route('/pygments.css')
def pygmentsCss():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run()
