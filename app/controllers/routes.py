from .. import app
from ..models import dbutils
from flask import request


@app.route('/addid', methods=['GET', 'POST'])
def add_id():
    if request.method == 'POST':
        if dbutils.add_new_device(request.form['reg_id'], 'active'):
            return '1'
        else:
            return '0'
    else:
        return '0'
