print("","Задание", "номер 1", "", sep="-+-+-+-")
info = input("Напишите любую ПОНЯТНУЮ информацию тут для того, чтобы узнать, какой тип он имеет: ")

def type_info(result1):
    return type(result1)
print("Данная информация имеет тип - ", type_info(info))

go = input("Хотите узнать количество байтов, байтовмассива, и занимаемой памяти этой информации? (Y/N): ")

if go == "Y":
    print(bytes(info , "utf-8"))
    print(bytearray(info , "utf-8"))
    print(memoryview(bytes(info , "utf-8")))
else:
    print("Так нет, значит нет - результата не будет!")
    pass