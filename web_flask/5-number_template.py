#!/usr/bin/python3
"""
This module creates a basic flask app that
gets dynamic route parameters and replaces
'_' with ' '
also displays an html page using template
"""
from flask import Flask, abort, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hi():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_route(text="is cool"):
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<n>', strict_slashes=False)
def num(n):
    try:
        number = int(n)
    except ValueError:
        abort(404)
    return f"{n} is a number"


@app.route('/number_template/<n>', strict_slashes=False)
def num_template(n):
    try:
        number = int(n)
    except ValueError:
        abort(404)
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
