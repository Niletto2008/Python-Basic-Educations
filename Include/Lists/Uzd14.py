Mylist = [1,2,3,4,5]
print("Original:","\n",Mylist)
print("Changes: ")
def Copy1():
    x = Mylist.copy()
    x.append(6)
    print(x)
Copy1()

def Copy2():
    y = Mylist
    y.append(6)
    print(y)
Copy2()