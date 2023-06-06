from datetime import datetime
from functools import reduce


def decorator(func):
    def func_decor():
        time1 = datetime.now()
        func()
        time2 = datetime.now()
        result = time2 - time1
        print(result)
    return func_decor()


@decorator
def factorial():
    reduce(lambda x, y: x * y, [i for i in range(1, 1001)])


@decorator
def even_num():
    filter(lambda x: x % 2 == 0, [i for i in range(1, 1001)])
