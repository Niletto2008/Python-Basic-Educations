def ExUzd2():
    try:
        summa = 0
        while True:
            i = int(input("Ievadi skaitlis: "))
            summa += i
            data = input("Vai vēlaties turpināt( Y/N ):  ")
            if data == "Y":
                pass
            elif data == "N":
                print("summa par visiem i skaitliem: ",summa)
                break
            else:
                print("Jūs ievadījāt nepareizu burtu, programma apstājās, ieslēdziet programmu vēlreiz!")
                break
    except ValueError:
        print("Jūs nepareizi ievadījāt i!")
ExUzd2()