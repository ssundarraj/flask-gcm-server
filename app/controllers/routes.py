from .. import app
from ..models import dbutils
from flask import request, render_template
from ..settings import APP_NAME

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', APP_NAME=APP_NAME)
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
