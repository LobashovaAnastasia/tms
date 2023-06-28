from dataclasses import dataclass

"""
1. Описать Dataclass, который
- содержит три произвольных поля, разных типов
- имеет один-единственный classmethod, который:
  - проверяет типы этих трех полей и возвращает объект Dataclass'a, если типы верны 
  - порождает исключение TypeError если хотя бы один из атрибутов имеет НЕВЕРНЫЙ тип
- является НЕИЗМЕНЯЕМЫМ (у инстанса этого класса нельзя изменить значения атрибута/добавить новый атрибут/удалить атрибут)
"""


@dataclass
class MyDataClass:
    a: str
    b: int
    c: list

    @classmethod
    def build(cls, a, b, c):
        if a == str(a) and b == int(b) and c == list(c):
            return a, b, c
        else:
            raise TypeError('Неверный тип атрибута')


person1 = MyDataClass.build("TEST", 34, [1, 2, 3])  # valid parameters
print(person1)
try:
    person2 = MyDataClass.build(100, 33, [1, 2, 3])  # invalid parameters
except Exception as exc:
    print(exc)

try:
    person3 = MyDataClass.build("TEST", "33", [1, 2, 3])  # invalid parameters
except Exception as exc:
    print(exc)

try:
    person3 = MyDataClass.build("TEST", 33, (1, 2, 3))  # invalid parameters
except Exception as exc:
    print(exc)
