def func():
    input_str = input('Введите строку: ')
    flag = True
    for i in input_str:
        if i.isdigit() or i == '.' or i == '-':
            flag = True
        else:
            flag = False
            print(f'Вы ввели не корректное число: {input_str}')
            break
    if flag:
        input_str = float(input_str)
        if input_str < 0 and int(input_str) == input_str:
            print(f'Вы ввели отрицательное целое число: {int(input_str)}')
        elif input_str > 0 and int(input_str) == input_str:
            print(f'Вы ввели положительное целое число: {int(input_str)}')
        elif input_str < 0 and float(input_str) == input_str:
            print(f'Вы ввели отрицательное дробное число: {float(input_str)}')
        elif input_str > 0 and float(input_str) == input_str:
            print(f'Вы ввели положительное дробное число: {float(input_str)}')


func()
