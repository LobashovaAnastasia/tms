import random
rand_num = random.randrange(1, 101)
print(rand_num)
inp_num = int(input('Введите целое число в диапазоне от 1 до 100: '))
while True:
    if inp_num == rand_num:
        print("Поздравляю! Вы угадали число!")
        break
    if inp_num > rand_num:
        inp_num = int(input("Ваше число больше загаданного. Попробуйте еще раз...  "))
    if inp_num < rand_num:
        inp_num = int(input("Ваше число меньше загадонного. Попробуйте еще раз...  "))
