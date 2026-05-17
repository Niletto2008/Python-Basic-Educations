
def uzd1(n):
    if n == 1:
        print("Stop function!", n)
    if n > 1:
        print("NONONO!!")
    if n != 1:
        uzd1(n + 1)
uzd1(1)


def uzd2(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * uzd2(a - 1)
print(uzd2(3))


def uzd3(c):
    summa = 0
    if c == []:
        return 0
    else:
        return sum(c)
d = [2,2,2]
print(uzd3(d))
