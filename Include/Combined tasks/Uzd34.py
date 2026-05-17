mylist = [6, True, 7, 8, "Skibidi", "gool", False, 7]
num = [6,7,8,7]
text = {"Skibidi", "gool"}

Mydict = {
    "int" : 4,
    "str" : 2
}

print(Mydict)

def uzd5():
    try:
        info = print("Введи ключ, чтобы узнать о нем инфу(int, str): ")
        data = str(input())
        match data:
            case "int":
                print("Данный ключ int содержит",Mydict["int"],"элемента")
            case "str":
                print("Данный ключ str содержит",Mydict["str"],"элемента")
            case _:
                print("Ты не то ввёл!")
    finally:
        print("GOOL")
uzd5()