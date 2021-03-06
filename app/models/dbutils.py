from .. import db
import device
import messages


def add_new_device(reg_id, status):
    new_user = device.Device(reg_id, status)
    db.insert({'user': new_user})
    print db.all()
    return 1
    return 0


def add_new_message(message_text):
    new_message = messages.Message(message_text)
    db.session.add(new_message)
    db.session.commit()
    return new_message.id


def get_all_messages():
    list_of_messages = messages.Message.query.all()
    return list_of_messages

