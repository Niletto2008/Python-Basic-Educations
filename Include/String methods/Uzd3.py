text = input("Введи любой текст на английском языке: ")

def TextCheck():
    if text:
        print("Длина строки и количество символов в тексте: " + (str(len(text))))
        print("Текст в верхнем регистре: " + (text.upper()))
        print("Текст в нижнем регистре: " + (text.lower()))
    else:
        print("ошибка!")

TextCheck()