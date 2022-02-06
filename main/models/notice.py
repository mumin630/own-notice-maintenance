from main import db


class Notice(db.Model):
    messageid = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    week = db.Column(db.String(3))
    time = db.Column(db.DateTime)
    message = db.Column(db.Text)
    sendtarget_logical = db.Column(db.String(50))
    sendchannel_logical = db.Column(db.String(50))

    # データを整形する
    def trim_data(notice_list):

        for index, notice in enumerate(notice_list):

            # 日付データの整形
            if (notice.date is None):
                notice_list[index].date = "-"

            # 時間データの整形
            notice_list[index].time = notice.time.strftime('%H:%M')

        return notice_list
