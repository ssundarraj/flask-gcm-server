from .. import app
from ..models import dbutils
from flask import request, render_template
from ..settings import APP_NAME

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # list_of_messages = dbutils.get_all_messages()
        return render_template('index.html', APP_NAME=APP_NAME, messages=list_of_messages)
    elif request.method == 'POST':
        print "Send GCM here"
        dbutils.add_new_message(request.form['notif_msg'])
        return '1'
    else:
        return '0'


@app.route('/addid', methods=['GET', 'POST'])
def add_id():
    if request.method == 'POST':
        if dbutils.add_new_device(request.form['reg_id'], 'active'):
            return '1'
        else:
            return '0'
    else:
        return '0'
