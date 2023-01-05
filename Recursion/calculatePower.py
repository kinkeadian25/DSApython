def calculatePower(base, exp):
    assert int(exp) == exp, 'exp must be an integer'
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/base * calculatePower(base, exp+1)
    else:
        return base * calculatePower(base, exp-1)

print(calculatePower(4, 2))
