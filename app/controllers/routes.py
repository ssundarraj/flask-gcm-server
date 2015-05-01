from .. import app
from ..models import dbutils
from flask import request

@app.route('/addid', methods=['GET', 'POST'])
def add_id():
    if request.method == 'POST':
        return dbutils.add_new_regid(request.form['reg_id'], 'active')
    else:
        return '1'
