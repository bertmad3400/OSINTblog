from flask import Flask
from flask_flatpages import FlatPages

app = Flask(__name__)

app.static_folder = "../static"
app.template_folder = "../templates"
