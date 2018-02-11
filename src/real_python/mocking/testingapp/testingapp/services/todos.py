import requests
from testingapp.constants import BASE_URL
# http://jsonplaceholder.typicode.com/
# curl -X GET 'http://jsonplaceholder.typicode.com/todos'



def get_todos():
    response = requests.get(f'{BASE_URL}/todos')
    if response.ok:
        return response

def get_uncompleted_todos(todos):
    resp = get_todos()
    print(resp)
    if not resp:
        return []
    else:
        todos = resp.json()
        return [todo for todo in todos if todo.get('completed' == False)]


