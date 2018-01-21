import pytest
import tasks
from tasks import Task

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()

def test_add_returns_valid_id(tasks_db):
    new_task = Task('Do something')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)

def test_added_task_has_id_set(tasks_db):
    new_task = Task('sit in chair', owner='toomas', done=True)
    task_id = tasks.add(new_task)

    task_from_db = tasks.get(task_id)
    assert task_from_db.id == task_id

def test_add_increases_count(db_with_3_tasks):
    tasks.add(Task('Throe a party'))
    assert tasks.count() == 4


