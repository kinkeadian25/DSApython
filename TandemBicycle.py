def tandemBicycle(red, blue, fastest):
    sol = 0
    blue.sort()
    red.sort(reverse = fastest)

    for i in range(len(red)):
        if blue[i] > red[i]:
            sol+=blue[i]
        else:
            sol+=red[i]
    return sol
