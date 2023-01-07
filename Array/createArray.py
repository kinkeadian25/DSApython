from array import *

#1. create an array and traverse
print("Step 1")
arr1 = array('i', [1,2,3,4,5])

for i in arr1:
    print(str(i) + ', ')
#2. access individual elements through indexes
print("Step 2")

print(arr1[0])
#3. append any value to the array using append() method
print("Step 3")

arr1.append(6)
print(arr1)
#4. insert value in an array using insert() method
print("Step 4")

arr1.insert(2, 8)
print(arr1)
#5. extend python array using extend() method
print("Step 5")

arr2 = array('i', [10,11,12])
arr1.extend(arr2)
print(arr1)
#6. add items from list into array using fromlist() method
print("Step 6")

items = [20, 21, 22]
arr1.fromlist(items)
print(arr1)
#7. remove any array element using remove() method
print("Step 7")
arr1.remove(22)
print(arr1)
#8. remove last array element using pop() method
print("Step 8")
arr1.pop()
print(arr1)
#9. fetch any element through its index using index() method
print("Step 9")
print(arr1.index(8))
#10. reverse a python array using reverse() method
print("Step 10")
arr1.reverse()
print(arr1)
#11. get array buffer information through buffer_info() method
print("Step 11")
print(arr1.buffer_info())
#12. check for number of occurrences of an element using count() method
print("Step 12")
print(arr1.count(6))
#13. convert array into string using tostring() method
print("Step 13")
strTemp = ''
for i in arr1:
    strTemp += str(i)
print(strTemp)
#14. convert array to a python list with same elements using tolist() method
print("Step 14")
arr1.tolist()
print(arr1)
