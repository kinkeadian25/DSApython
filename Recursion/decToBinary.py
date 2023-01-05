def dToB(n):
    assert int(n) == n, 'The parameter must be an int only'
    if n == 0:
        return 1
    else:
        return n%2 + 10 * dToB(int(n/2))

print(dToB(1.3)) 
