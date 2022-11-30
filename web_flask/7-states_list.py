#!/usr/bin/python3
"""
    flask app
"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown(self):
    """
        storage close
    """
    from models import storage
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """
        state_list route
    """
    from models import storage
    from models.state import State
    states = storage.all(State).values()
    return render_template(
        "7-states_list.html",
        states=states), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
