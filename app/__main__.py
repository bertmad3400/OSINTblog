from flask import Flask, render_template

from app import app, flatpages


@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/post/")
def listPosts():
    print(list(flatpages))
    posts = [p for p in flatpages if p.path.startswith(app.config["POST_DIR"])]
    posts.sort(key=lambda item:item['date'], reverse=False)
    return render_template('postList.html', posts=posts)

@app.route('/post/<string:name>/')
def post(name):
    path = '{}/{}'.format(app.config["POST_DIR"], name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)

if __name__ == "__main__":
    app.run()
