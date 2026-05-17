name = str(input("Просим ввести вам тут свое имя пользователя: "))

def NameCheck1():
    if len(name) == 0:
        print("Строка пуста!")
    else:
        print("Строка заполнена!")

NameCheck1()

def NameCheck2():
    if len(name) > 3:
        print("Строка имеет больше 3 символов!")
    else:
        print("Строка НЕ имеет больше 3 символов!")

NameCheck2()
