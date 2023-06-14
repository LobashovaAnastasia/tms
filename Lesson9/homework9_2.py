import time
from homework9_1 import Auto


class Truck(Auto):
    obj1 = 'Object1'
    obj2 = 'Object2'

    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
        Auto.__init__(self, brand, age, mark, color=None, weight=None)
        self.max_load = max_load

    def move(self):
        print('attention', end=' ')
        super().move()

    def load(self):
        time.sleep(1)
        print("Load")
        time.sleep(1)


class Car(Auto):
    obj1_ = 'Object1_'
    obj2_ = 'Object2_'

    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):
        Auto.__init__(self, brand, age, mark, color=None, weight=None)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'Max speed is {self.max_speed}')
