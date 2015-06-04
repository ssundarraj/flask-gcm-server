#!/usr/bin/env python
import os

settings_string = """INSTALLED = True
APP_NAME = '{APP_NAME}'
API_KEY = '{API_KEY}'
DATA_STORE = '{DATA_STORE}'
TINYDB_PATH = '{TINYDB_PATH}'
"""
APP_NAME = None
API_KEY = None
DATA_STORE = 'TinyDB'
TINYDB_PATH = os.path.join(os.getcwd(), 'db.json')

APP_NAME = raw_input("Enter the name of the app: ")
API_KEY = raw_input("Enter GCM API Key: ")

settings_string = settings_string.format(**locals())

with open('./app/settings.py', 'w') as settings_file:
    settings_file.write(settings_string)

print "To change any of the settings edit the file './app/settings.py'"
