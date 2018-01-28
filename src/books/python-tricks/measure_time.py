from time import time, sleep

# FIXIT
class Alpha:
    def __init__(self):
        self.start = 0
        self.end = 0

    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time()
        return self

    def runtime(self):
        sleep(1)
        elapsed = self.end - self.start
        print(elapsed)


def alpha():
    print('asd')

with Alpha() as timeit:
    timeit.runtime()


