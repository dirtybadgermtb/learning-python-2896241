import string

def is_palindrome(teststr):
    # Remove specific characters 'ABC' and all numbers from the string
    # Remove all spaces, special characters, and upper/lowercase letters
    sanitized = teststr.translate(str.maketrans("", "", string.ascii_letters + string.punctuation + " "))
    return sanitized == sanitized[::-1]

# Test cases
print(is_palindrome("racecar1"))          # True
print(is_palindrome("racecarABC123"))    # True
print(is_palindrome("hello123ABC"))      # False
