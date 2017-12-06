import logging.config
import logging

from flask import Flask, url_for, request, render_template, Markup
import json


app = Flask(__name__)

logging.config.fileConfig('myapp.cfg')
logger = logging.getLogger('myapplication')


@app.route('/notify', methods=['POST'])
def listener():
    request_data =  request.get_data()
    logger.info(request_data)




"""
# Could not get it to work - but the tests were green!
def create_app():
    app = Flask(__name__)

    @app.route('/notify', methods=['POST'])
    def listener():
        return request.get_data()
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5000)
"""
