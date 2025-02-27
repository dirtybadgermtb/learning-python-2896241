#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def func1():
    print("I am a function") # This line must be indented to belong to the function

# TODO: function that takes arguments
def func2(arg1, arg2):
    print(arg1," ",arg2)

# TODO: function that returns a value
def cube(x):
  return x * x * x
  
# TODO: function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result  # This line should be at the same indentation level as the for loop

# TODO: function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

# func1() # Prints "I am a function" to the console
# print(func1()) # Prints "I am a function" followed by "None" (default return value)
# print(func1) # Prints the function object itself, e.g., <function func1 at 0xe1a0e8>

# func2(10, 20)
# print(func2(10,20))
# print(cube(3))

# print(power(2))
# print(power(2,3))

# print(power(x=3, num=2)) # This is an example of named arguments

print(multi_add(4,5,10,4,10))
    