def count_num():
    list_num = [0, 0, 8, 8, 7, 4, 5, 5, 1, 2, 3, 4, 1]
    res = {'zero': 0, 'one': 0, 'two': 0, 'three': 0, 'four': 0,
           'five': 0, 'six': 0, 'seven': 0, 'eight': 0, 'nine': 0}
    for i in list_num:
        if i == 0:
            res['zero'] += 1
        if i == 1:
            res['one'] += 1
        if i == 2:
            res['two'] += 1
        if i == 3:
            res['three'] += 1
        if i == 4:
            res['four'] += 1
        if i == 5:
            res['five'] += 1
        if i == 6:
            res['six'] += 1
        if i == 7:
            res['seven'] += 1
        if i == 8:
            res['eight'] += 1
        if i == 9:
            res['nine'] += 1
    print(res)


count_num()
