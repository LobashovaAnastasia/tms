str_1 = input('Введите строку 1: ')
str_2 = input('Введите строку 2: ')
str_3 = input('Введите строку 3: ')
str_4 = input('Введите строку 4: ')


with open(
        'result_file.txt',
        mode='w',
        encoding='utf-8'
) as file:
    file.write(str_1 + '\n')
    file.write(str_2 + '\n')
file.close()


with open(
        'result_file.txt',
        mode='a',
        encoding='utf-8'
) as file:
    file.write(str_3 + '\n')
    file.write(str_4)
file.close()
