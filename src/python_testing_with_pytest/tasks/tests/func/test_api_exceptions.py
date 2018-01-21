import pytest
import tasks

def test_add_raises():
    with pytest.raises(TypeError):
        tasks.add(task='no Task object')

def test_start_tasks_db_raises():
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db('my/test/path', 'postgres')
    exception_msg = excinfo.value.args[0]
    assert exception_msg == 'db_type must be "tiny" or "mongo"'

@pytest.mark.smoke
def test_list_raises():
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)

@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    with pytest.raises(TypeError):
        tasks.get(task_id='123')
