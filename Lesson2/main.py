# СРЕЗЫ
my_string = "aaaaaBccBddBeeBffBggB"
print(my_string[5::3])

my_string2 = "AAAABBBBCCCCDDDDFFFF"
print(my_string2[:4] + my_string2[4:8] + my_string2[8:12] + my_string2[12:16] + my_string2[16:20])

my_string3 = "PYTHON"
print(my_string3[::-1])

# Lesson2
#ex_1
a = 3
b = a
c = a
print(id(a), id(b), id(c))
#ex_2
a = 5
b = [a]
print(id(a), id(b))
#ex_3
a = 3
b = str(a)
c = [a]
print(id(a), id(b), id(c))

a = 5
b = a
print(id(a), id(b))
#ex_4
a = input('Введите строку: ')
my_str1 = a[::2]
my_str2 = a[1::2]
print("Введенная строка:", a.strip())

print('Четные символы: ', my_str2)
print('Нечетные символы: ', my_str1)