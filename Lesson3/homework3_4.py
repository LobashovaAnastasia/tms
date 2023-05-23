num = int(input("Введите целое число: "))
num_2 = num

result_1 = 0
while num:
    result_1 += num**3
    num -= 1
print(result_1)

result_2 = 0
for x in range(1, num_2 + 1):
    result_2 += x**3
print(result_2)

