Numbers = [4,9,2,4,0,3,4,1]

def NonSorted(y):
    return Numbers
Numbers.sort(key=NonSorted)
print(Numbers)

def Sorted(x):
    x.sort()
    print(x)
Sorted(Numbers)