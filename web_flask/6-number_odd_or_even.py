#!/usr/bin/python3
"""
Flask instance
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_isfun(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    if n.isnumeric():
        return "{} is a number".format(n)
    return "", 404


@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    if n.isnumeric():
        return render_template("5-number.html", data=n)
    return "", 404

@app.route("/number_odd_or_even/<n>")
def odd_even(n):
    if n.isnumeric():
        if int(n) % 2 == 0:
            return render_template("6-number_odd_or_even.html",data = f"{n} is even")
        return render_template("6-number_odd_or_even.html",data = f"{n} is odd")   

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
