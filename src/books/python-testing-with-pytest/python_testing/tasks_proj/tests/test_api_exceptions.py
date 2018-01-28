import pytest
import tasks

class TestUpdtate():

    def test_bad_id(self):
        with pytest.raises(TypeError):
            tasks.update(
                task_id={'dict_instead': 1},
                task=tasks.Task(),
            )

    def task_bad_task(self):
        with pytest.raises(TypeError):
            tasks.update(task_id=1, task='not a task')



