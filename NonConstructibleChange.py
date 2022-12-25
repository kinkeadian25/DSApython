def nonConstructibleChange(coins):
    coins.sort()
    change = 0
    for coin in coins:
        if coin > change + 1:
            break
        else:
            change += coin
    return change + 1
