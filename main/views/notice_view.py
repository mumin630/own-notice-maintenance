import flask
from main import app
from main.models.notice import Notice


@app.route('/notice')
def show_notice():
    notice = Notice

    # お知らせの一覧を取得する
    notice_list = notice.query.all()

    # 取得したデータを整形する
    notice_list = notice.trim_data(notice_list)

    return flask.render_template('notice.html', notice_list=notice_list)
