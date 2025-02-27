# Solution to programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#


def is_palindrome(teststr):
    # Your code goes here
    # convert the string to all lower case
    teststr = teststr.lower()

    
    # strip all the spaces and punctuation from the string
    newstr = ""
    for x in teststr:
        if x.isalnum():
            newstr += x

    # Now calculate the reverse of the string
    reversestr = ""
    strindx = len(newstr)-1
    while (strindx >= 0):
        reversestr += newstr[strindx]
        strindx -= 1

  #The active selection is a conditional statement in Python that checks if two strings, newstr and reversestr, are equal.
    if newstr == reversestr:
        return True
    return False

print(is_palindrome("Radar"))   # Expected True
print(is_palindrome("Race car!"))   # Expected True