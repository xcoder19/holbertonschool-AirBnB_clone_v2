#!/usr/bin/python3
"""flask app"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def states_list():
    data = storage.all(State)
    return render_template("7-states_list.html",data = data)



@app.teardown_appcontext
def teardown():
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
