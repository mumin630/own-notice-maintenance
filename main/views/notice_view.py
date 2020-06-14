import flask
from main import app, db
from main.models.notice import Notice


@app.route('/notice')
def show_notice():
    notice_list = Notice.query.all()
    return flask.render_template('notice.html', notice_list=notice_list)
