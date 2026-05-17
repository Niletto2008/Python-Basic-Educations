parole = input("Введите пароль: ")

def CheckParole():
    if len(parole) > 8:
        print("Пароль больше 8 символов!")
    else:
        print("Пароль не принят, так как имеет меньше 8 символов!")
    
    res1 = parole.isalnum()
    print("Содержит ли пароль хотя бы одну цифру: " + str(res1))
    res2 = parole.isalpha()
    print("Содержит ли пароль хотя бы одну букву(Данная строка может выдать неправильный ответ): " + str(res2))

CheckParole()