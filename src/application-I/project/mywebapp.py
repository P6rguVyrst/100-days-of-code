#!/usr/bin/env python3
# -*- coding: utf8 -*-

import logging.config
import logging
import json
import os
#from pathlib import PurePath


from flask import (
    Flask,
    jsonify,
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


def media_request(data):
    """Handle media request"""

    return 'Media request accepted'

def contact_request(data):
    """Handle contact request"""


    return 'Contact request accepted'

def parse_request(data):

    return_message = {'errors': []}
    msg_type = data.get('msg_type', {})
    body = data.get('body', {})

    actions = {
        'media': media_request,
        'contact': contact_request,
    }

    keys = [key for key in actions]

    if msg_type:
        if not msg_type in keys:
            return_message['errors'].append({'message': 'Unsupported value for {}'.format('msg_type')})
        else:
            print('hello')
            return_message['message'] = actions[msg_type](data)
    else:
        return_message['errors'].append({'message': 'Missing key {}'.format('msg_type')})

    if not return_message['errors']:
        return_message.pop('errors')

    return return_message

@app.route('/notify', methods=['GET', 'POST'])
def listener():

    if request.method == 'POST':
        data = json.loads(request.get_data(as_text=True))
        res = parse_request(data)
        if res.get('errors'):
            return jsonify(res), 415
        else:
            LOGGER.info(data)
            # Writing directly to file because could not get rsyslog to route socket messages to file.
            #with open("/var/log/100daysofcode.log", "a") as myfile:
            #    myfile.write(str(data) + '\n')

            return jsonify(res), 201
    else:
        return jsonify({'message': "POST me a message."}), 200

@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
    )
