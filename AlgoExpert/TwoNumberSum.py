def twoNumberSum(array, targetSum):
    test = set(array)

    for i in range(len(array)):
        checkSum = targetSum - array[i]
        if checkSum in test and array[i] != checkSum:
            return[checkSum, array[i]]
    
    return []
