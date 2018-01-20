import pytest
from tasks import Task

@pytest.mark.xfail()
def test_task_equality():
    t1 = Task('sit down', 'toomas')
    t2 = Task('get up', 'ormisson')
    assert t1 == t2


@pytest.mark.xfail()
def test_dict_equality():
    t1_dict = Task('sit down', 'toomas')._asdict()
    t2_dict = Task('sit down', 'joonas')._asdict()
    assert t1_dict == t2_dict


