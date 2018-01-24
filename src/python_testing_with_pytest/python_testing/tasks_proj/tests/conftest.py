import json
import pytest
import tasks
from tasks import Task


#@pytest.fixture()
#def tasks_db(tmpdir):
#    tasks.start_tasks_db(str(tmpdir), 'tiny')
#    yield
#    tasks.stop_tasks_db()

@pytest.fixture(scope='session', params=['tiny', 'mongo'])
def tasks_db_session(tmpdir_factory, request):
    temp_dir = tmpdir_factory.mktemp('temp')
    tasks.start_tasks_db(str(temp_dir), request.param)
    yield
    tasks.stop_tasks_db()

@pytest.fixture()
def tasks_db(tasks_db_session):
    tasks.delete_all()

@pytest.fixture(scope='session')
def tasks_just_a_few():
    return (
        Task('Write some code', 'Toomas', True),
        Task('Review code', 'Waldo', False),
        Task('Fix code', 'Mario', False),
    )

@pytest.fixture(scope='session')
def tasks_mult_per_owner():
    return (
        Task('Write some code', 'Toomas'),
        Task('Review code', 'Toomas'),
        Task('Fix code', 'Toomas'),

        Task('Write some code', 'Waldo'),
        Task('Review code', 'Waldo'),
        Task('Fix code', 'Waldo'),

        Task('Write some code', 'Mario'),
        Task('Review code', 'Mario'),
        Task('Fix code', 'Mario'),
    )

@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    for t in tasks_just_a_few:
        tasks.add(t)

@pytest.fixture()
def db_with_multi_per_owner(tasks_db, tasks_mult_per_owner):
    for t in tasks_mult_per_owner:
        tasks.add(t)

'''
def pytest_adoption(parser):
    group = parser.getgroup('nice')
    group.addoption('--nice', action='store_true', help='nice: turn failures into opportunities...')

def pytest_report_header():
    if pytest.config.getoption('nice'):
        return 'Thank you for smoking.'

def pytest_report_teststatus(report):
    if report.when == 'call':
        if report.failed and pytest.config.getoption('nice'):
            return (report.outcome, 'O', 'OPPORTUNITY for improvement')
'''

