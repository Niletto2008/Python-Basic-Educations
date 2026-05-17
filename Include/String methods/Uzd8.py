text = "I love Python and hate Assembler!"

def CheckText1():
    print(len(text))
    print(text.count("a"))
    print(text.find("Python"))
    
    text2 = text.replace("Python", "Java")
    print(text2)

CheckText1()

def CheckText2():
    res = None
    if len(text) > 10:
        res = True
        print(res)
    else:
        res = False
        print(res)

CheckText2()