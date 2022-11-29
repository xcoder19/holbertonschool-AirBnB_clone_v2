#!/usr/bin/python3
"""flask app"""


from flask import Flask

""" app instance """
app = Flask(__name__)

"""/ route"""


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """/ route"""

    return "Hello HBNB!"


"""/hbnb route"""


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """/hbnb route"""
    return "HBNB"


"""c_is func route """


@app.route("/c/<text>", strict_slashes=False)
def c_isfun(text):
    """c_is func route """
    text = text.replace("_", " ")
    return f"C{text}"


"""host and port"""


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
