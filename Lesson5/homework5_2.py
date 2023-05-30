input_number = int(input('Введите число: '))
res = 1


def fact_num(num):
    if num >= 1:
        global res
        res *= num
        fact_num(num - 1)
    else:
        print(res)


fact_num(input_number)
