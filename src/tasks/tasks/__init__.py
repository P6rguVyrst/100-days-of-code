# -*- coding: utf-8 -*-

"""Top-level package for Tasks Project."""

from .api import (
    Task,
    TasksException,
    add,
    get,
    list_tasks,
    count,
    update,
    delete,
    delete_all,
    unique_id,
    start_tasks_db,
    stop_tasks_db
)



__author__ = """Toomas Ormisson"""
__email__ = 'Toomas.Ormisson@gmail.com'
__version__ = '0.1.0'


