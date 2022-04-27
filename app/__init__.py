from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)

app.static_folder = "../static"
app.template_folder = "../templates"

DEBUG = True

app.config.update(  DEBUG = DEBUG,
                    FLATPAGES_AUTO_RELOAD = DEBUG,
                    FLATPAGES_EXTENSION = ".md",
                    FLATPAGES_ROOT = "../content",
                    POST_DIR = "posts" )


flatpages = FlatPages(app)
freezer = Freezer(app)
