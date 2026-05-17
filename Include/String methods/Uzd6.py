text = input("Введи текст с пробелами в начале и в конце: ")

def lidz():
    print("Текст до обработки: " + text)
    print("Размер текста до обработки: " + str(len(text)))
lidz()

def pec():
    res1 = text.strip(" ")
    print("Текст после обработки: " + res1)
    print("Размер текста после обработки: " + str(len(res1)))
pec()