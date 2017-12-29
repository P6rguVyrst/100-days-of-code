from __future__ import absolute_import, unicode_literals
from .celery import app


@app.task
def add(x, y):
    return x + y

@app.task
def mul(x, y):
    return x * y

@app.task
def xsum(numbers):
    return sum(numbers)

@app.task
def gen_prime(x):
    multiples = []
    results = []
    for i in range(2, x+1):
        if i not in multiples:
            results.append(i)
            for j in range(i*i, x+1, i):
                multiples.append(j)
    return results

@app.task
def test():
    pass

#test_task = test.signature(args=(1, 2, 3), queue='high', immutable=True)
#test_task.apply_async()

