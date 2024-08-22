#!/usr/bin/python3
"""
This module is to create a basic flask app
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
