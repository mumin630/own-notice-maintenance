from main import db


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)

    def __repr__(self):
        return "<Test id={} title={!r}>".format(self.id, self.title)
