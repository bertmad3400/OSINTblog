from flask import Flask, render_template_string, Markup
from flask_flatpages import FlatPages, pygmented_markdown
from flask_frozen import Freezer

app = Flask(__name__)


def prerender_jinja(text):
    prerendered_body = render_template_string(Markup(text))
    return pygmented_markdown(prerendered_body)


app.static_folder = "../static"
app.template_folder = "../templates"

DEBUG = False

app.config.update(
    DEBUG=DEBUG,
    FLATPAGES_AUTO_RELOAD=DEBUG,
    FLATPAGES_EXTENSION=".md",
    FLATPAGES_ROOT="../content",
    POST_DIR="posts",
    FLATPAGES_HTML_RENDERER=prerender_jinja,
    FREEZER_DESTINATION="../build",
    FREEZER_RELATIVE_URLS=False,
)

flatpages = FlatPages(app)
freezer = Freezer(app)
