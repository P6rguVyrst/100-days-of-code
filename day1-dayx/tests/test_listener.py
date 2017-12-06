from flask import Flask, request, url_for

app = Flask(__name__)

class TestListener(object):
    def test_listener(self, client):
        res = client.post(url_for('listener'))
        assert request.path == '/notify'
        assert  request.method == 'POST'

