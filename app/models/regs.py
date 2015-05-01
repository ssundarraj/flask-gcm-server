from .. import db


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reg_id = db.Column(db.String(1024), index=True, unique=True)
    status = db.Column(db.String(64), index=True,)

    def __init__(self, reg_id, status):
        self.reg_id = reg_id
        self.status = status

    def __repr__(self):
        return '<Device {0}>'.format(self.id)
