class MyException(Exception):
    pass


try:
    first_num = float(input('Введите первое число: '))
    operator = input('Введите операцию: ')
    second_num = float(input('Введите второе число: '))
    if operator == '+':
        print(first_num + second_num)
    elif operator == '-':
        print(first_num - second_num)
    elif operator == '*':
        try:
            res = first_num * second_num
            res.add(0)
        except AttributeError as err:
            raise MyException('Неверный атрибут!')
    elif operator == '/':
        try:
            print(first_num / second_num)
        except ZeroDivisionError:
            print("Деление на ноль!")
    else:
        print('Неверная операция!')
except ValueError:
    print('Вы ввели не корректное значение!')
