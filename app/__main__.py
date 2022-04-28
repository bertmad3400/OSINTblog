from flask import Flask, render_template
from flask_flatpages import pygments_style_defs

import werkzeug

import sys

from app import app, flatpages, freezer

def getPage(pageName):
    return flatpages.get_or_404(f"{app.config['POST_DIR']}/{pageName}")

@app.errorhandler(werkzeug.exceptions.HTTPException)
def handleHTTPErrors(e):
    return render_template("error.html", errorCode=e.code, errorName=e.name, errorDescription=e.description), e.code

@app.route("/")
def homepage():
    return render_template("post.html", post=getPage("homepage"))

@app.route("/post/")
def listPosts():
    posts = [p for p in flatpages if p.path.startswith(app.config["POST_DIR"])]
    posts.sort(key=lambda item:item['date'], reverse=False)
    return render_template('postList.html', posts=posts)

@app.route('/post/<string:name>/')
def post(name):
    return render_template('post.html', post=getPage(name))

@app.route("/about/")
def about():
    return render_template("post.html", post=getPage("about"))

@app.route('/pygments.css')
def pygmentsCss():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run()
