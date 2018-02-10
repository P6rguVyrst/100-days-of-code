from unittest.mock import Mock, patch
from testingapp.services.todos import get_todos

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
@patch('testingapp.services.todos.requests.get')
def test_getting_todos_when_response_is_ok(mock_get):
    todos = [{
        'userId': 1,
        'id': 1,
        'title': 'Make the bed',
        'completed': False
    }]
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = todos
    response = get_todos()
    assert isinstance(response.json(), list)


