def function1():
    dict_ = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    empty_dict = {}
    for name, value in dict_.items():
        empty_dict.update({value: name})
    print(empty_dict)


function1()
