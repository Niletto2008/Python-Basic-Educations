def uzd1():
    mylist = [2,2,7,9,0,3,4,9]
    myset = set((mylist))
    print(myset)
    myset = list((myset))
    print(myset)
    print(len(myset))
uzd1()

def uzd2():
    mytuple = ("Kaka", "Olivia", "Tun Tun")
    print(mytuple)
    list1 = list(mytuple)
    list1[2] = "Zabzila"
    print(list1)
    list1 = tuple((list1))
    print(list1)
uzd2()

def uzd3():
    commands = dict(com1 = "start", com2 = "stop", com3 = "help")
    info = print("Введите команду(help, start, stop): ")
    data = input()
    match data:
        case "start":
            print("Вы выполнили команду старт!")
        case "stop":
            print("Вы выполнили команду стоп!")
        case "help":
            print("Вы выполнили команду Хелп!")
        case _:
            print("Не выполненна ни одна команда!")
uzd3()