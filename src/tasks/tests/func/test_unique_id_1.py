import pytest
import tasks
from tasks import Task


@pytest.mark.xfail(tasks.__version__ < '0.2.0',
                   reason='not supported until  version 0.2.0')
def test_unique_id():
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2

@pytest.mark.skip(reason='Misunderstood the API')
def test_unique_id1():
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


def test_unique_id_2():
    ids = []
    ids.append(tasks.add(Task('One')))
    ids.append(tasks.add(Task('Two')))
    ids.append(tasks.add(Task('Three')))
    uid = tasks.unique_id()
    assert uid not in ids

@pytest.mark.xfail()
def test_unique_id_is_a_duck():
    uid = tasks.unique_id()
    assert uid == 'a duck'

