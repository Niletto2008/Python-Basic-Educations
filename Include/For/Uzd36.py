def uzd5():
    data = str(input("Введите строку: "))
    info1 = None
    info2 = None
    for i in data:
        print(i)
        if i.isdigit():
            info1 = True
        if i.isalpha():
            info2 = True
    print(info1)
    print(info2)
uzd5()

def uzd6():
    mylist = [x for x in range(1,11)]
    print(mylist)
uzd6()

def uzd7():
    mylist2 = [2,7,4,8,0,3,2,8,4]
    mytuple = [i for i in mylist2]
    mytuple = tuple(mytuple)
    print(mytuple)
uzd7()

def uzd8():
    mydict = dict(d = 4, a = 5)
    for u in mydict.items():
        print(u)
uzd8()        