from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery(
    'myapp',
    broker='pyamqp://guest@localhost//',
    include=['myapp.tasks'],

)
#app = Celery('myapp',
#             broker='amqp://',
#             backend='amqp://',
#             include=['myapp.tasks'])

app.conf.update(
    result_expires=3600,

)

if __name__ == '__main__':
    app.start()
