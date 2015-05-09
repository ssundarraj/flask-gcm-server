#!/usr/bin/env python
from app import app
from app import db
from app import settings

if not settings.INSTALLED:
    print "Please execute install.py to install the server."
else:
    print "Starting server"
    app.run()
