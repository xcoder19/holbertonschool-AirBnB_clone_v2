#!/usr/bin/python3
"""flask app"""
from flask import Flask
""" instance of Flask class"""
app = Flask(__name__)
"""/ route"""


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


"""hbnb route"""


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


"""c route"""


@app.route("/c/<text>", strict_slashes=False)
def c_isfun(text):
    text = text.replace("_", " ")
    return f"C{text}"


"""host and port """
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
