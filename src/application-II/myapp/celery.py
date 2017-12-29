from __future__ import absolute_import, unicode_literals
from celery import Celery
from kombu import Queue

app = Celery(
    'myapp',
    broker='pyamqp://guest:guest@localhost//',
    include=['myapp.tasks'],

)
#app = Celery('myapp',
#             broker='amqp://',
#             backend='amqp://',
#             include=['myapp.tasks'])

ROUTING_TABLE = {
    'myapp.tasks.add': {'queue': 'hipri'},
    'myapp.tasks.test': {
        'exchange': 'high',
        'exchange_type': 'high',
        'routing_key': 'high',
    },

}
app.conf.task_default_queue = 'default'
app.conf.task_queues = (
    Queue('default', routing_key='task.#'),
    Queue('feed_tasks', routing_key='feed.#'),
)

task_default_exchange = 'tasks'
task_default_exchange_type = 'topic'
task_default_routing_key = 'task.default'

app.conf.update(
    result_expires=3600,
    task_routes = ROUTING_TABLE,

)

if __name__ == '__main__':
    app.start()
