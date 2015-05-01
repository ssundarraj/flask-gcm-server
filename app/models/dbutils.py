from .. import db
import regs


def add_new_device(reg_id, status):
    new_user = regs.Device(reg_id, status)
    db.session.add(new_user)
    db.session.commit()
    return new_user.id
