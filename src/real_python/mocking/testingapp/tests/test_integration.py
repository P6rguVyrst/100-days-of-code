from unittest.mock import Mock, patch
from unittest import skipIf
from testingapp.constants import SKIP_REAL

from testingapp.services.todos import (
    get_todos,
    get_uncompleted_todos,

)


# Working mocking example.
@skipIf(SKIP_REAL, 'Skipping tests that hit real API')
def test_integration_contract(todos_api_response):
    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    actual = get_todos()
    actual_keys = actual.json().pop().keys()
    with patch('testingapp.services.todos.requests.get') as mock_get:
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = todos_api_response
        mocked = get_todos()
        mocked_keys = mocked.json().pop().keys()
    assert actual_keys == mocked_keys


