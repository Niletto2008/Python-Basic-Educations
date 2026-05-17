
def uzd1(n):
    for x in range(n):
        yield x
a = uzd1(3)
for b in a:
    print(b)

def uzd2():
    for x in range(21):
        if x % 2 == 0:
            yield x
b = uzd2()
for z in b:
    print(z)

def uzd3():
    text = ["Hello", "aboaba", "apple", "albonos","Olivia", "elprimo"]
    for x in text:
        if len(x) > 5:
            yield x
c = uzd3()
for z in c:
    print(z)