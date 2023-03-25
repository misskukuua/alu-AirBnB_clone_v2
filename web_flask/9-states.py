#!/usr/bin/python3
"""
    Start Flask
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displays an Html page with a all the states"""
    State = storage.all("State")
    return render_template("9-states.html", state=State)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """HTML page with info about id"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def close_session(response_or_exc):
    """ Request to remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
