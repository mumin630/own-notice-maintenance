import flask
from main import app, db
from main.models.test import Test


@app.route('/test')
def show_test():
    test_list = Test.query.all()
    return flask.render_template('test.html', test_list=test_list)


@app.route('/test/add', methods=['POST'])
def add_test():
    test = Test(
        title=flask.request.form['title'],
        text=flask.request.form['text']
    )
    db.session.add(test)
    db.session.commit()
    return flask.redirect(flask.url_for('show_test'))
