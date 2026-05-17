def Errors():
    try:
        print("Введите число: ")
        data = int(input())
    except ValueError:
        print("Вы вввели не число!!")
    else:
        print("Вы всё ввели правильно!")
Errors()