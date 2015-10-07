import json
from tinydb.serialize import Serializer


class Device(object):
    def __init__(self, reg_id=0, status=0):
        self.reg_id = reg_id
        self.status = status

    def __repr__(self):
        return json.dumps({'reg_id': self.reg_id, 'status': self.status})


class DeviceSerializer(Serializer):
    OBJ_CLASS = Device

    @staticmethod
    def encode(obj):
        return json.dumps({'reg_id': obj.reg_id, 'status': obj.status})

    @staticmethod
    def decode(s):
        j = json.loads(s)
        return Device(j['reg_id'], j['status'])
