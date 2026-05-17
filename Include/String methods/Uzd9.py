text = input("Введите текст(строку): ")

def Rezultat():
    rez1 = text.upper()
    print("1.) ", rez1)
    rez2 = text.lower()
    print("2.) ", rez2)
    rez3 = text.swapcase()
    print("3.) ", rez3)
    rez4 = text.strip(" ")
    print("4.) ", rez4)
    rez5 = text.ljust(20)
    print("5.) ", rez5)
    rez6 = text.rjust(20)
    print("6.) ", rez6)
    rez7 = text.rjust(20, "0")
    print("7.) ", rez7)
Rezultat()

def Rezultat2():
    rez8 = text.isalpha()
    rez9 = text.isdigit()
    rez10 = text

    if rez8:
        print("Строка состоит только из букв!")
    else:
        print("Строка НЕ состоит только из букв (учитывая пробелы)!")

    if rez9:
        print("Строка состоит только из цифр!")
    else:
        print("Строка НЕ состоит только из цифр!")

    if rez10 == "":
        print("Строка пуста!")
    else:
        print("Строка не пуста!") 

Rezultat2()