# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False] #the first element of an index is 0. This goes back to the C programming language where arrays are 0-based
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)
# print(mylist)
# print(mytuple)
# print(mydict)

# # re-declaring a variable works
# myint = "abc"
# print(myint)

# To access a member of a sequence type, use []
# print(mylist[2])    # Prints the 3rd element of the list (index starts at 0)
# print(mytuple[1])   # Prints the 2nd element of the tuple (index starts at 0)

# # Use slices to get parts of a sequence
# print(mylist[1:5])  # Prints elements from index 1 up to (but not including) index 5
# print(mylist[1:5:2])  # Prints every 2nd element from index 1 up to (but not including) index 5
      
# # you can use slices to reverse a sequence
# print(mylist[::-1])

# dictionaries are accessed via keys
# print(mydict["one"])  

# ERROR: variables of different types cannot be combined
# print("string type" + 123)  # This will cause an error because you cannot concatenate a string with an integer. In other words, you cannot combine data types. 
#lets fix this error by including the str() function to convert the integer to a string
# print("string type" + str(123))

# Global vs. local variables in functions
def someFunction():
    global mystr
    mystr = "def"
    print(mystr)

someFunction()  # This will print "def"
print(mystr)    # This will print "This is a string"

del mystr
print(mystr)    # This will cause an error because the variable mystr has been deleted. ie NameError: name 'mystr' is not defined