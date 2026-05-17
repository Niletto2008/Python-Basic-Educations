def uzd1():
    for a in range(1,11):
        print(a)
uzd1()

def uzd2():
    info1 = "Hello World!"
    for b in info1:
        print(b)
uzd2()

def uzd3():
    mylist1 = [1,6,9,0,3,5,7]
    summa = 0
    for c in mylist1:
        print(c)
        summa += c
    print(summa)
uzd3()

def uzd4():
    mylist2 = [5,4,9,0,2,3,7]
    for d in mylist2:
        if d % 2 == 0:
            print(d)
    print("Stop!")
    for e in mylist2:
        if e % 2 != 0:
            print(e)
uzd4()
