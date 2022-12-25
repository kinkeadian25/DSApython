def minimumWaitingTime(queries):
    queries.sort()
    time = 0
    newTime = 0

    for i in range(len(queries) - 1):
        time += queries[i]
        newTime += time
    
    return newTime
