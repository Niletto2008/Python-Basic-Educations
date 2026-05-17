print("Задание","номер 2.2", end="", sep="-+-+-+-")
print(":")
x = int(input("Введи первое число: "))
y = int(input("Введи второе число: "))
quest = input("Выбери, каким путем решить решение (+,-,*, /): ")

print("Результат: ")

if quest == "+":
    res1 = lambda a,b: a + b
    itog1 = res1(x,y)
    print(itog1)

if quest == "-":
    res2 = lambda a,b: a - b
    itog2 = res2(x,y)
    print(itog2)

if quest == "*":
    res3 = lambda a,b: a * b
    itog3 = res3(x,y)
    print(itog3)

if quest == "/":
    res4 = lambda a,b: a / b
    itog4 = res4(x,y)
    print(itog4)

if quest == " ":
    pass