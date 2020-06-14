import flask
from main import app, db


@app.route('/')
def show_index():
    return flask.render_template('index.html')


def init():
    db.create_all()
