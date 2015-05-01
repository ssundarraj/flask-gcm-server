from .. import db
import device


def add_new_device(reg_id, status):
    new_user = device.Device(reg_id, status)
    db.session.add(new_user)
    db.session.commit()
    return new_user.id
