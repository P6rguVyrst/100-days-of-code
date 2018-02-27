from hanoi import hanoi
from time import time

start = time()
r = hanoi(20)
end = time()
runtime = end - start
print(r)
print('runtime: {}s'.format(runtime))
