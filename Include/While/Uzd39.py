def uzd6():
    i = 0
    while True:
        i = input("Введите число или числа: ")
        if not i.isdigit():
            break
        elif i == "-":
            break
        elif i != "-":
            print("Вы написали положительно число",i)
uzd6()