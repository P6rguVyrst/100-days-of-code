from collections import Counter
from heapq import merge

def elements_count(*lists):

    try:
        return {k: int(v)-1 for k, v in dict(Counter(list(merge(*lists)))).items() if v > 1}
        print('aaa')
    except TypeError:
        return {}


list_one = [1, 3, 5, 7, 9, 11]
list_two = [3, 4, 5, 6, 7]
list_three = [5, 6, 7, 8, 9, 10]
#x = elements_count(list_one, list_two, list_three)
x = elements_count(list_one)#, list_two, list_three)
print(x)
