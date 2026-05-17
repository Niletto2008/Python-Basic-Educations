myset1 = set(("apple", "cocomelon", "watermelon"))
myset2 = set((1,3,8,8,6,7))

print(myset1 | myset2 )
print(myset1.isdisjoint(myset2))
print(myset1.difference(myset2))
print(not(myset1.isdisjoint(myset2)))