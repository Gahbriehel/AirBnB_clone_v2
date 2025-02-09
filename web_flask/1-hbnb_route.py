#!/usr/bin/python3
"""
This module adds a new route to the flask app
and returns HBNB
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hi():
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
