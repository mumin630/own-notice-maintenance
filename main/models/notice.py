from main import db


class Notice(db.Model):
    messageid = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    week = db.Column(db.String(3))
    time = db.Column(db.DateTime)
    message = db.Column(db.Text)
    sendtarget = db.Column(db.String(50))
    sendchannel = db.Column(db.String(50))

    def __repr__(self):

        format = "<Notice "
        format += "message_id={} "
        format += "date={} "
        format += "week={} "
        format += "time={} "
        format += "message={} "
        format += "send_target={} "
        format += "send_channel={} "
        format += ">"

        return format.format(
            self.messageid,
            self.date,
            self.week,
            self.time,
            self.message,
            self.sendtarget,
            self.sendchannel
        )
