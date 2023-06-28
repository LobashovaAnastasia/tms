import datetime


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def year_of_birth(self):
        date_ = datetime.datetime.now()
        return date_.year - self.age

    def __gt__(self, value):
        return value.age < self.age

    def __lt__(self, value):
        return value.age > self.age

    def __ge__(self, value):
        return value.age <= self.age

    def __le__(self, value):
        return value.age >= self.age

    def __eq__(self, value):
        return value.age == self.age and value.name.lower() == self.name.lower()

    def __ne__(self, value):
        return value.age != self.age or value.name.lower() != self.name.lower()


person1 = Person('Alex', 34)
# ==
assert person1 == Person('Alex', 34)
assert person1 == Person('alex', 34)
assert person1 == Person('ALEX', 34)
# !=
assert person1 != Person('Alex!', 34)
assert person1 != Person('Alex', 35)
# >
assert person1 > Person('Alex', 33)
assert person1 > Person('Ann', 33)
# <
assert person1 < Person('Alex', 35)
assert person1 < Person('Ann', 35)
# >=
assert person1 >= Person('Alex', 34)
assert person1 >= Person('Alex', 33)
assert person1 >= Person('Ann', 34)
assert person1 >= Person('Ann', 33)
# <=
assert person1 <= Person('Alex', 34)
assert person1 <= Person('Alex', 35)
assert person1 <= Person('Ann', 34)
assert person1 <= Person('Ann', 35)
