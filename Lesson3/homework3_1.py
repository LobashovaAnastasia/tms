input_string = input('Введите предложение: ')
spase = input_string.find(' ')
first_word = input_string[:spase]
second_word = input_string[spase + 1:]
print("! {} ! {} !".format(second_word, first_word))
print(f"! {second_word} ! {first_word} !")
print("! %s ! %s !"%(second_word, first_word))
print('!', second_word, "!", first_word, "!")