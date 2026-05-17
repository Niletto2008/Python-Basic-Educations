import re

def uzd41():
    data = False
    x = input("Введите строку на английской языке(запрещенно в начале и в конце применять пробелы, а то программа даст неправильный результат): ")
    mylist = []

    for num in x:
        if re.findall("\d", num):
            mylist.append(num)
        elif num.isspace():
            print("Ошибка! В тексте содержится пробел, уберите его пожалуйста, чтобы получить правильный и точный результат!")
            break

    if len(mylist) == len(x):
        data = True

    print(mylist)
    print(data)
uzd41()