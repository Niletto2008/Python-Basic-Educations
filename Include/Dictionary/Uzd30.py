mydict1 = {
    "name" : "John",
    "ID" : "5346453-36434",
    "age" : 25
}

mydict2 = {
    "green" : "watermelon",
    "red" : "apple",
    "yellow" : "lemon"
}

print(mydict1) 

mydict3 = mydict1 | mydict2
print(mydict3)

mydict1.update(mydict2)
print(mydict1)
