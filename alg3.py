import math
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 0:
        return False
    mid_index = math.floor(len(aStr)/2)
    mid = aStr[mid_index]
    if char == mid:
        return True
    elif len(aStr) == 1:
        return False
    else:
        if char < mid:
            aStr = aStr[:mid_index]
        else:
            aStr = aStr[mid_index:]
        return isIn(char, aStr)
