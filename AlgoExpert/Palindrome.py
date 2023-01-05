def isPalindrome(string):
    start = 0
    end = len(string) - 1

    while start <= end:
        if len(string) == 1:
            return True
        if string[start] == string[end]:
            start+=1
            end-=1
        else:
            return False
            
    return True
