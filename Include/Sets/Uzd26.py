myset1 = "I love, 1 2 3, Merry Christmas!"
myset2 = "I love Merry Christmas!"
myset3 = "1 2 3"
myset4 = ""

res1 = set((myset2))
print(res1)
res2 = set((myset3))
print(res2)

res3 = res1 | res2
print(res3)

res4 = myset4.join(res3)
print(res4)