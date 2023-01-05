def firstNonRepeatingCharacter(string):
    dict = {}

    for char in string:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    for char in string:
        if dict[char] == 1:
            return string.index(char)
    return -1
