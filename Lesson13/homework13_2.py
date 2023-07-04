import random


class RandomValue:
    def __init__(self):
        self.limit = my_limit
        self.counter = 0

    def __iter__(self):
        while self.counter < self.limit:
            result = random.randint(0, 99)
            self.counter += 1
            yield result
        print("Iterator is stopped!")


my_limit = int(input("Введите лимит: "))
my_random = RandomValue()

results = [elem for elem in my_random]
print(results)

assert len(results) == my_limit
for i in results:
    assert i is not None
