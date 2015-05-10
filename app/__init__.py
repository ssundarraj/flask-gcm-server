import os
import settings
from flask import Flask
app = Flask(__name__)

from flask.ext.sqlalchemy import SQLAlchemy

if settings.DATA_STORE is 'sqlite':
    db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'app.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + db_path

db = SQLAlchemy(app)

import controllers.routes
import models.device
import models.messages

app.debug = True
if __name__ == '__main__':
    app.run(debug=True)
