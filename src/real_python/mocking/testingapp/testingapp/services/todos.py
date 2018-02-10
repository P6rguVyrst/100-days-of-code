import requests
from testingapp.constants import BASE_URL
# http://jsonplaceholder.typicode.com/
# curl -X GET 'http://jsonplaceholder.typicode.com/todos'



def get_todos():
    response = requests.get(f'{BASE_URL}/todos')
    if response.ok:
        return response


