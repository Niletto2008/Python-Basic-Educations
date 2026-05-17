import re

def parole():
    x = input("Введите пароль: ")
    a = re.findall("\s", x)
    b = re.findall("\d", x)
    if a and b:
        print("Пароль соотвествует!")
    else:
        print("Пароль не подходит!")
parole()

def search():
    w = "Today, I want play with 3 friends, whose are 16 years old, game \" 20980 Titule \" !"
    info = []
    data = re.findall("[a-zA-Z]", w)
    if data:
        info.append(data)
    print(info)
search()
