print("Задание","номер 2.1", end="", sep="-+-+-+-")
print(":")
x = int(input("Введи первое число: "))
y = int(input("Введи второе число: "))
quest = input("Выбери, каким путем решить решение (+,-,*, /): ")

print("Результат: ")

if quest == "+":
    def summa(a,b):
        return a + b
    res1 = summa(x,y)
    print(res1)


if quest == "-":
    def minus(a,b):
        return a - b
    res2 = minus(x,y)
    print(res2)


if quest == "*":
    def umnoz(a,b):
        return a * b
    res3= umnoz(x,y)
    print(res3)


if quest == "/":
    def delenie(a,b):
        return a / b
    res4 = delenie(x,y)
    print(res4)

if quest == " ":
    pass