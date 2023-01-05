def sortedSquaredArray(array):
    sol = [0] * len(array)
    end = len(array) - 1
    start = 0
    idx = len(array) - 1
    while start <= end:
        startSqr = array[start] * array[start]
        endSqr = array[end] * array[end]

        if startSqr > endSqr:
            sol[idx] = startSqr
            start+=1
            idx-=1
        else:
            sol[idx] = endSqr
            end-=1
            idx-=1
            
    return sol
