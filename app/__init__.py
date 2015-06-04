import os
import settings
from flask import Flask
from tinydb import TinyDB
app = Flask(__name__)

db = TinyDB(settings.TINYDB_PATH)

import controllers.routes

app.debug = True
if __name__ == '__main__':
    app.run(debug=True)
