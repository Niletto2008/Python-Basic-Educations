def uzd1():
    i = 1
    while i < 11:
        print(i)
        i += 1
uzd1()

def uzd2():
    a = 0
    while a <= 5:
        print(a)
        a += 1
uzd2()

def uzd3():
    data = None
    while data != "0":
        if input("Введите числа: ") == "0":
            print("Вы вышли из цикла!")
            break
uzd3()