#!/usr/bin/python3
"""
    flask app
"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown(self):
    """
        storage close
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """
        state_list route
    """
    data = storage.all("State")
    return render_template("7-states_list.html", data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
