a = 5 
b = 6
z = int(input("Введи в z переменную любое число: "))
o = int(input("Введи во o переменную любое число: "))

def Uzd1():
    print("1.) ", a + b)
    print("2.) ", a - b)
    print("3.) ", a * b)
    print("4.) ", a / b)
    print("5.) ", a // b)
    print("6.) ", a % b)
    print("7.) ", a ** b)
Uzd1()

def Uzd2():
    print("2.1.) ", a > b)
    print("2.2.) ", a < b)
    print("2.3.) ", a == b)
    print("2.4.) ", a != b)
    print("2.5.) ", a <= b)
    print("2.6.) ", a >= b)
Uzd2()

def Uzd3():
    print("3.1.) ", a < b and b != a)
    print("3.2.) ", a > b or a < b)
    print("3.2.) ", not(a > b))
Uzd3()

def Uzd4():
    num = 10
    num += 10
    print("4.1.) ", num)
    num -= 10
    print("4.2.) ", num)
    num *= 10
    print("4.3.) ", num)
    num /= 10
    print("4.4.) ", num)
    num //= 10
    print("4.5.) ", num)
    num %= 2
    print("4.6.) ", num)
Uzd4()

def Uzd5():
    x = "OMG! Merry Christmas!"
    print("5.1.) " , "e" in x)
    print("5.2.) " , "Merry" in x)
    print("5.3.) " , "m" not in x)
Uzd5()

def Uzd6():
    c = 6
    d = c
    print("6.1.) " , c is d)
    print("6.2.) " , c is not d)
Uzd6()

def Uzd7():
    if z > o:
        print("z переменная больше, чем о!")
    elif z == o:
        print("Оба переменных равны")
    else:
        print("о больше, чем z!")
    
    if z % o == 0:
        print("Числа делятся без остатка!")
    else:
        print("Числа не делятся, есть остаток!")
Uzd7()