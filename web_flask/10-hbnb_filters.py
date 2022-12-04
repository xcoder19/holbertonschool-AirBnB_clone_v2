#!/usr/bin/python3
"""flask app"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    from models import storage
    from models.state import State
    from models.city import City
    list_state = []
    state_dict = storage.all(State)
    for k, v in state_dict.items():
        list_state.append(v)

    list_citie = []
    city_dict = storage.all(City)
    for k, v in city_dict.items():
        list_citie.append(v)
    return render_template("8-cities_by_states.html", states=list_state,
                           cities=list_citie)


@app.teardown_appcontext
def teardown(exception):
    from models import storage
    from models.state import State
    from models.city import City
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
