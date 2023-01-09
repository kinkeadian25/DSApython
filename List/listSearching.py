myList = [10,20,30,40,50,60,70,80,90]

# if 20 in myList:
#     print(myList.index(20))
# else:
#     print('the value does not exist')

def linearSearch(myList, value):
    for i in myList:
        if i == value:
            return myList.index(value)
    return 'value doesnt exist'

print(linearSearch(myList, 20))