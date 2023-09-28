from flask import Flask
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/about")
def about():
    return "<p>This app is a CPP degree calculator</p>"
