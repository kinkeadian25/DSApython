def greatestCommonDiv(a,b):
    assert int(a) == a and int(b) ==b, 'the numbers must be integer only'
    if a < 0:
        a = a * -1
    if b < 0:
        b = b * -1
    if b == 0:
        return a
    else:
        return greatestCommonDiv(b, a%b)

print(greatestCommonDiv(18, 48))