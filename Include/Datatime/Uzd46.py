import datetime
import re

def uzd1():
    x = datetime.datetime.now()
    res1 = x.strftime("%Y")
    res2 = x.strftime("%B")
    res3 = x.strftime("%d")
    res4 = x.strftime("%H.%M")
    print(res1)
    print(res2)
    print(res3)
    print(res4)
uzd1()


def uzd2():
    x = datetime.datetime.now()
    res1 = x.strftime("%d.%m.%Y")
    print(res1)
uzd2()

def uzd3():
    a = int(input("Введи год: "))
    b = int(input("Введи месяц: "))
    c = int(input("Введи число дня: "))
    d = datetime.datetime(a,b,c)
    print(d)
    x = datetime.datetime.now()
    print(x)
    data = x - d
    print(data.days,"days")
uzd3()

def uzd4():
    try:
        x = input("Введи дату (YYYY-MM-DD): ")
        y = datetime.datetime.strptime(x, "%Y-%m-%d")
    except ValueError:
        print("Неправильный синтаксис!")
    else:
        print("Всё правильно!")
        print(y)
uzd4()

def uzd5():
    txt = "Today, 26.12.2025, I want to write a 2 home works at 12.01.2026 ! "
    search = re.findall("\d+.\d+.\d+", txt)
    print(search)
    for x in search:
        y = datetime.datetime.strptime(x, "%d.%m.%Y")
        print(y.year,"-",y.month,"-",y.day)
uzd5()