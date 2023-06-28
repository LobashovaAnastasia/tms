class Parent1:
    person = 'Person'


class Parent2:
    person = 'Person'


class Parent3:
    person = 'Person'


class MyClass(Parent1, Parent2, Parent3):
    person = 'Person'

    def __init__(self, person: str):
        self.person = person

    def get_attribute(self, attr_name: str):
        if attr_name in self.__dict__:
            print(f"Attribute {attr_name} found in Instance: {self}")
            return self.__dict__[attr_name]
        if attr_name in self.__class__.__dict__:
            print(f"Attribute {attr_name} found in Instance Class: {self.__class__.__name__} ")
            return self.__class__.__dict__[attr_name]
        for attr in self.__class__.mro()[1:0]:
            if attr_name in attr.__dict__:
                print(f"Attribute {attr_name} found in Instance Parent Class: {attr.__name__}")
                return attr.__dict__[attr_name]
        raise AttributeError(f"{attr_name} not FOUND!")

