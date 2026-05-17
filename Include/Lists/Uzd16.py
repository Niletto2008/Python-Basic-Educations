Mylist1 = [1,5,6,0,2]
Mylist2 = ["a", "b", "c", "d", "e"]

def New1():
    Mylist3 = Mylist1 + Mylist2
    print(Mylist3)
New1()

def New2():
    Mylist1.extend(Mylist2)
    print(Mylist1)
New2()