myList = ['a','b', 'c', 'd', 'e', 'f']

myList[0:2] = ['x', 'y']

print(myList[:])

myList.pop()
print(myList)

del myList[2:4]
print(myList)

myList.remove('y')
print(myList)