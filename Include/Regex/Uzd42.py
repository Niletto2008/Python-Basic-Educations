import re

def uzd42():
    x = "i have pasport, whose saved information about my birthday in 2008 year!"
    mylist = []
    for num in x:
        if re.search("\d", num):
            mylist.append(num)
    if len(mylist) > 0:
        print("В тексте есть числа")
        print(mylist)
    else:
        print("В тексте чисел неимеется!")
uzd42()
