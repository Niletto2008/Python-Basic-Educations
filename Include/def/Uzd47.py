import time

def set_data1(func):
    def mywrap():
        result = func()
        if result == None:
            print("Функция ничего не вернула!")
        else:
            print("Результат:",result)
        return result
    return mywrap

@set_data1
def uzd1():
    return 1
uzd1()

def set_data2(data):
    summa = 0
    def res():
        nonlocal summa
        summa += data()
        print("Summa:",summa)
        return summa
    return res

@set_data2
def step1():
    return 1
step1()
step1()

def set_data3(data):
    def clock():
        start = time.perf_counter()
        end = time.perf_counter()
        x = data()
        x = print(f"{end - start}")
        return x
    return clock

@set_data3
def uzd3():
    return None
print(uzd3())

def set_data4(text):
    def message():
        txt = text().strip(" ").upper()
        print(txt)
        return txt
    return message

@set_data4
def uzd4():
    return "   Hello World!    "
uzd4()