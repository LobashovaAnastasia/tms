import random


class RandomValue:
    def __init__(self):
        self._list = [el for el in range(1, 101)]

    def __iter__(self):
        return RandomValueIterator(self._list)


class RandomValueIterator:
    def __init__(self, some_list):
        self._some_list = some_list
        self.limit = my_limit
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            result = self._some_list[random.randint(0, 99)]
            self.counter += 1
            return result
        else:
            print("Iterator is stopped!")
            raise StopIteration


my_limit = int(input("Введите лимит: "))
my_random = RandomValue()

results = [elem for elem in my_random]
print(results)

assert len(results) == my_limit
for i in results:
    assert i is not None
