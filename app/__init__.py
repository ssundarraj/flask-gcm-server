import os
import settings
from flask import Flask
from tinydb import TinyDB
from tinydb.storages import JSONStorage
from tinydb.middlewares import SerializationMiddleware
import models.device

app = Flask(__name__)


serialization = SerializationMiddleware()
serialization.register_serializer(models.device.DeviceSerializer, 'TinyDevice')
db = TinyDB(settings.TINYDB_PATH, storage=serialization)

import controllers.routes

app.debug = True
if __name__ == '__main__':
    app.run(debug=True)
