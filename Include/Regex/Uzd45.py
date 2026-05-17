import re

def uzd1():
    email = input("Введите свою почту: ")
    if re.search("gmail.com", email) and re.findall("[@]", email) and email.endswith("@gmail.com"):
        print("Адрес почты правильный!")
    else:
        print("Адрес почты НЕ правильный!")
uzd1()

def uzd2():
    txt = "Today, I want play with 3 friends, whose are 16 years old, game \" 20980 Titule \" !"
    y = re.findall("[0-9]", txt)
    x = []
    if y:
        x.append(y)
        print(x)
uzd2()


def uzd3():
    info = " I love Python"
    a = re.sub("Python" , "PYTHON", info)
    print(a)
uzd3()

def uzd4():
    number = input("Введите свой номер: ")
    b = re.findall("[+]371", number)
    if b and len(number) == 12:
        print("Номер был правильно написан!")
        print(number)
    elif not b and len(number) == 8:
        print("Номер был правильно написан, но уже в сокращенном виде!")
        print(number)
    else:
        print("Номер был НЕ правильно написан!")
uzd4()

def uzd5():
    text = "Today, I want play with 3 friends, whose are 16 years old | game Minecraft !"
    d = re.split("[,|]", text)
    print(d)
uzd5()

def uzd6():
    txt2 = "today today I want play play the game."
    g = re.findall("today today", txt2)
    h = re.findall("play play", txt2)
    if g and h:
        print("today")
        print("play")
uzd6()


def uzd7():
    print("Введите дату по частям!")
    dd = input("День: ")
    mm = input("Месяц: ")
    yy = input("Год: ")
    data = dd + "." + mm + "." + yy
    check = re.findall("\d", data)
    if not check or len(mm) != 2 or len(dd) != 2 or len(yy) < 1:
        print("Неправильно написал дату!!")
    else:
        print("Всё правильно, дата введенна!")
        print(data)
uzd7()


def uzd8():
    string = "Today, I want play with 3 friends, whose are 16 years old, game \" 20980 Titule \" !"
    z = re.split("[ ,\d]", string)
    mylist = []
    for i in z:
        if len(i) >= 4 and len(i) <= 7:
            mylist.append(i)
    print(mylist)
uzd8()