import pytest
from codeclub.second.delta import ATM

@pytest.fixture(scope='session')
def atm():
    return ATM()

