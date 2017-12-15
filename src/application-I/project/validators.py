#!/usr/bin/env python3
# -*- coding: utf8 -*-
from functools import wraps
from flask import (
    current_app,
    jsonify,
    request,
)

"""SOURCE:
https://stackoverflow.com/questions/24238743/flask-decorator-to-verify-json-and-json-schema
"""


def ValidationError(Exception):
    pass

def BadRequest(Exception):
    pass

def validate(*args):
    pass

def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            request.json
        except BadRequest as e:
            msg = "payload must be a valid json"
            return jsonify({"error": msg}), 400
        return f(*args, **kw)
    return wrapper

def validate_schema(schema_name):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            try:
                validate(request.json, current_app.config[schema_name])
            except ValidationError as e:
                return jsonify({"error": e.message}), 400
            return f(*args, **kw)
        return wrapper
    return decorator
