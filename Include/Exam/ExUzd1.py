def ExUzd1():
    try:
        summa = 0
        num = int(input("Ievadi veselu skaitlis a: "))
        num += 1
        for x in range(1, num, 1):
            if x % 2 != 0:
                summa += x
        print(summa)
    except ValueError:
        print("Klūda!!!")
ExUzd1()