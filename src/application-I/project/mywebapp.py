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
from json2html import *
from validators import (
    validate_json,
    validate_schema,
)


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
            return_message['errors'].append(
                {'message': 'Unsupported value for {}'.format('msg_type')}
            )
        else:
            return_message['message'] = actions[msg_type](data)
    else:
        return_message['errors'].append(
            {'message': 'Missing key {}'.format('msg_type')}
        )

    if not return_message['errors']:
        return_message.pop('errors')

    return return_message



if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
    )
