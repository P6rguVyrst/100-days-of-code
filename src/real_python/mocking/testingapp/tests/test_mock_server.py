
import requests


#def test_request_response():
#    url = 'http://localhost:{port}/users'.format(port=mock_server_port)
#    resp = rqquests.get_url(url)
#    assert resp.ok


####################

from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
from threading import Thread

class MockServerRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(requests.codes.ok)
        self.end_headers()

def get_free_port():
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    address, port = s.getsockname()
    s.close()
    return port

class TestMockServer(object):
    @classmethod
    def setup_class(cls):
        #Configure mock server
        cls.mock_server_port = get_free_port()
        cls.mock_server = HTTPServer(
            ('localhost', cls.mock_server_port),
            MockServerRequestHandler
        )

        cls.mock_server_thread = Thread(
            target=cls.mock_server.serve_forever
        )
        cls.mock_server_thread.setDaemon(True)
        cls.mock_server_thread.start()

    def test_request_response(self):
        url = 'http://localhost:{port}/users'.format(
            port=self.mock_server_port
        )
        response = requests.get(url)
        print(response)
        assert response.ok

