text = "I love Python"

def CheckText1():
    text1 = text.replace("I","*") 
    rez1 = text1.replace("P","*") 
    print(rez1)

    rez2 = rez1.replace(" ", "_")
    print(rez2)

    rez3 = rez2.count("*")
    print(rez3)
    rez4 = rez2.count("_")
    print(rez4)

CheckText1()

def CheckText2():
    ch = str.maketrans("o", "^")
    rez5 = text.translate(ch)
    print(rez5)
CheckText2()

def CheckText3():
    rez6 = text[0]
    print(rez6)
    rez7 = text[12]
    print(rez7)

    rez8 = len(text)
    print(rez8)

    rez9 = False
    if text.startswith("I") and text.endswith("I"):
        rez9 = True
        print(rez9)
    else:
        print(rez9)

CheckText3()