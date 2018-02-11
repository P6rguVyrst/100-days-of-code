from unittest.mock import Mock, patch
from testingapp.services.todos import (
    get_todos,
    get_uncompleted_todos,

)

def test_request_response():
    response = get_todos()
    assert response
#    response = requests.get('http://jsonplaceholder.typicode.com/todos')
#    assert response.ok

@patch('testingapp.services.todos.requests.get')
def test_request_response_mocked(mock_get):
    mock_get.return_value.ok = True
    response = get_todos()
    assert response

def test_request_response_mocked1():
    with patch('testingapp.services.todos.requests.get') as mock_get:
        mock_get.return_value.ok = True
        response = get_todos()
    assert response

def test_request_response_mocked2():
    mock_get_patcher = patch('testingapp.services.todos.requests.get')
    mock_get = mock_get_patcher.start()
    mock_get.return_value.ok = True
    response = get_todos()
    mock_get_patcher.stop()
    assert response

# use fixtures
@patch('testingapp.services.todos.get_todos')
def test_getting_todos_when_response_is_ok(mock_get, todos_api_response):
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = todos_api_response
    response = get_todos()
    assert isinstance(response.json(), list)

@patch('testingapp.services.todos.get_todos')
def test_getting_uncomplleted_todos_when_todos_is_not_none(
    mock_get_todos,
    todos_api_response,
    ):
    mock_get_todos.return_value = Mock()
    mock_get_todos.return_value.json.return_value = todos_api_response
    #print(mock_get_todos.return_value)
    #print(todos_api_response)
    uncompleted_todos = get_uncompleted_todos(todos_api_response)
    #print(uncompleted_todos)
    assert mock_get_todos

@patch('testingapp.services.todos.get_todos')
def test_getting_uncomplleted_todos_when_todos_is_none(
    mock_get_todos,
    todos_api_response,
    ):
    mock_get_todos.return_value = None
    #print(todos_api_response)
    uncompleted_todos = get_uncompleted_todos(None)
    #print(uncompleted_todos)
    assert mock_get_todos


class TestTodos:
    @classmethod
    def setup_calss(cls):
        cls.mock_get_patcher = patch('testingapp.services.todos.requests.get')
        cls.mock_get = cls.mock_get_patcher.start()
    @classmethod
    def teardown_class(cls):
        cls.mock_get_patcher.stop()




