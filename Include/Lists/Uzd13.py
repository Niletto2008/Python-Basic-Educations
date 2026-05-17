mylist = [x for x in range(1,11)]
print("Список чисел от 1 до 10: ","\n", mylist)

def Uzd1():
    res1 = [y**2 for y in mylist ]
    print("1.)","\n", res1)
    res2 = [z for z in mylist if z % 2 == 0]
    print("2.)","\n",res2)

Uzd1()

