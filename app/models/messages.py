from .. import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message_text = db.Column(db.String(1024), index=True,)

    def __init__(self, message_text):
        self.message_text = message_text

    def __repr__(self):
        return '<Message {0}>'.format(self.id)
