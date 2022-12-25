def classPhotos(red, blue):
    big = red if max(red) > max(blue) else blue
    small = red if max(red) < max(blue) else blue

    big.sort()
    small.sort()
    
    for i in range(len(big)):
        if big[i] - small[i] <= 0:
            return False

    return True
