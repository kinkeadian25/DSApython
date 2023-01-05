def isValidSubsequence(array, sequence):
    start = 0
    for i in range(len(array)):
        if array[i] == sequence[start]:
            start += 1
        if start == len(sequence):
            return True
            
    return False
