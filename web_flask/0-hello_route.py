#!/usr/bin/python3
"""flask app"""
from flask import Flask

app = Flask(__name__)
"""/route"""


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
