mydict = dict(name = "John", age = 22, country = "Latvia" )

print(mydict)
del mydict["country"]
print(mydict)
mydict.pop("age")
print(mydict)
mydict["email"] = "John228@gmail.com"
print(mydict)
mydict.clear()
print(mydict)