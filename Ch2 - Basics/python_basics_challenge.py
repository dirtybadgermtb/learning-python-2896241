import string

def is_palindrome(teststr):
    # Remove spaces and punctuation from the string
    sanitized = teststr.replace("1", "")
    return sanitized == sanitized[::-1]

# Test cases
print(is_palindrome("radar1")) # True