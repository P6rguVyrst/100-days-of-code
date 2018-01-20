
from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

class TasksException(Exception):
    pass

def add(task): pass

def get(task_id): pass

def list_tasks(owner=None): pass

def count(): pass

def update(task_id, task): pass

def delete(task_id): pass

def delete_all(): pass

def unique_id(): pass

def start_tasks_db(db_path, db_type): pass

def stop_tasks_db(): pass


