while True:
    name = input("Введите свое имя: ")
    age = input("Введите свой возраст: ")
    check_age = age.isdigit()
    if not check_age or int(age) <= 0:
        print('Ошибка повторите ввод')
    elif int(age) < 10:
        print(f"Привет, шкет {name}")
    elif int(age) <= 18:
        print(f"Как жизнь {name}?")
    elif int(age) < 100:
        print(f"Что желаете {name}?")
    else:
        print(f"{name}, вы лжете - в наше время столько не живут...")
