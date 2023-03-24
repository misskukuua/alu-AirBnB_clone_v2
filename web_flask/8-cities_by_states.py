#!/usr/bin/python3
""" Flask web app"""

from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
        States/cities sorted by name
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states.values())


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
