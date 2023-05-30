from datetime import datetime
from time import sleep


def func():
    n = int(input("Введите количество элементов: "))
    res = []
    for _ in range(n):
        res.append(datetime.strftime(datetime.now(), f'%Y-%m-%d %H:%M:%S'))
        sleep(1)
    print(res)


func()
