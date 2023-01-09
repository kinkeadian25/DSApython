# a=[1,2,3]
# b=[4,5,6]

# c= a+b
# print(c)

# a = [0,1]
# a = a * 4
# print(a)

a = [0,1,2,3,4,5,6]
print(min(a))
print(max(a))
print(len(a))
print(sum(a)/len(a))

myList = []
while (True):
    inp = input('Enter a number, or done to get the average of numbers: ')
    if inp == 'done': break
    value = float(inp)
    myList.append(value)
print('Average', sum(myList)/len(myList))