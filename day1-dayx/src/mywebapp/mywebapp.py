#!/usr/bin/env python3
# -*- coding: utf8 -*-

import logging.config
import logging
import json
import os
#from pathlib import PurePath


from flask import (
    Flask,
    url_for,
    request,
    render_template,
    Markup,
)
from validators import (
    validate_json,
    validate_schema,
)

#CWD = os.getcwd()
#ROOT = PurePath(CWD).parents[0]
CFG = 'conf/myapp.cfg'
logging.config.fileConfig(CFG)

app = Flask(__name__)
LOGGER = logging.getLogger('myapplication')


activate_schema = app.config.update(dict(
    message=str(),
))


def media_request():
    return 'Media request'

def contact_request():
    return'Contact request'

def parse_request(data):
    # Data is a bytes object. Fix it. Ensure dict. Validators not working.
    return_message = {'errors': []}
    msg_type = data.get('msg_type', {})
    body = data.get('body', {})

    actions = {
        'media': media_request(),
        'contact': contact_request(),
    }

    if msg_type in actions.keys():
        return_message['message'] = actions[msg_type]
    else:
        return_message['errors'].append({'message': 'Unsupported message type'})

    return return_message


@validate_json
@validate_schema('activate_schema')
@app.route('/notify', methods=['GET', 'POST'])
def listener():
    data = request.get_data()
    if request.method == 'POST':
        res = parse_request(data)
        return res
    else:
        return "POST me a message."

if __name__ == '__main__':
    app.run()
