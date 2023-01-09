numList = [1,2,3,4,5,6,8,9,10]

# def FindMissingNum(numList):
#     for i in range(len(numList)):
#         if numList[i] != i+1:
#             return i+1
        
#     return 0

# print(FindMissingNum(numList))

def findMissing(numList, n):
    sum1=n*(n+1)/2
    sum2=sum(numList)
    print(sum1-sum2)

findMissing(numList, len(numList)+1)
        
        