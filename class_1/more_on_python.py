#!/usr/bin/env python3
# coding: utf-8
"""Introduction to Python - Continuation"""


# Data Structures
# A Data Structure is a variable that can store information in a specific manner.
# Different Data Structures serve different purposes, and have different advantages.

# The most simple data structure is the list:
# A List in Python is created using square brackets ([]) and all items inside are separated using commas (,):
list_1 = [1, 2, 3]
list_2 = ["a", "b", "c"]

# Lists can have any size, even being empty, and items inside may be of different types:
list_3 = []  # empty list
list_4 = [1, "a", True]  # random list
list_5 = [None]  # not empty list, but with no values


# Similar to lists, and oversimplifying, a tuple is an immutable* version of a list
# It's written with parenthesis instead of square brackets, although, we can also create without the parenthesis
# Immutable means that, once created, the value of these objects is permanent and cannot be modified.
tuple_example = (1, 2, 3, 4)
tuple_example_2 = 1, 2, 3, 4  # same tuple, created without parenthesis

# For tuples with a single item, a final comma must be added to the end of the expression
tuple_example_3 = (1, )

# Since parenthesis may also be used to group an expression, it's recommended that we explicitly cast a list as tuple
tuple_example_4 = tuple([1, 2, 3, 4])


# More on mutable/immutable variables:
list_x = [1, 2, 3]
list_x[0] = 5
print(list_x)
# We can see the above code changes the first element of `list_x` to 5, meaning the list_x is mutable

# If we try doing this with a tuple, an exception will be thrown
list_y = tuple([1, 2, 3])
try:
    # try running this code, and it will produce an error on this line
    list_y[0] = 5

except TypeError as err:

    print("Error:", err)
print(list_y)


# Another very useful Data Structure in Python is the dictionary (dict)
# A dict can be created using curly brackets ({})
# The keys and values are defined using a colon (:) and separated with commas, as follows:
dict_1 = {}  # empty dict
dict_2 = {"key1": "value1", "key 2": 2}
# Python's dict keys must be immutable, and the values may be anything, including other dicts!

# Dicts can be a value in a list:
list_with_dict = [{"id": 1}, {"id": 2}]

# Lists can be a value in a dict:
dict_with_list = {"numbers": [1, 2, 3]}

# Both lists and dicts can be defined along multiple lines
# If it improves readability, or to separate items like a sublist, such as:
# list example:
long_list = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    ["a", "b", "c", "d", "e", "f", "g", "h", "j"]
]

# instead of:
long_list_2 = [[1, 2, 3, 4, 5, 6, 7, 8, 9], ["a", "b", "c", "d", "e", "f", "g", "h", "j"]]

# dict example
long_dict = {
    "numbers": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "letters": ["a", "b", "c", "d", "e", "f", "g", "h", "j"]
}

# instead of:
long_dict_3 = {"numbers": [1, 2, 3, 4, 5, 6, 7, 8, 9], "letters": ["a", "b", "c", "d", "e", "f", "g", "h", "j"]}

# For more details on Data Structures in Python: https://docs.python.org/3/tutorial/datastructures.html


# Python Operators
# To compare values/variables, in programming, we use operators
# The most important Python operators are ("a" and "b" are example variables):
# a == b : compares if variables a and b have the same values
# a != b : compares if variables a and b have different values
# a > b  : compares if variable a has a value bigger than b's value
# a < b  : compares if variable a has a value lower than b's value
# a >= b : compares if variable a has a value bigger or equal to b's value
# a <= b : compares if variable a has a value lower or equal to b's value

# To compare if a variable has a null value, it's common to use the "is" keyword, as follows:
# a is None


# Operators are commonly used in flow control
# Python uses the if/elif/else nomenclature for flow control
# elif and else are optional, and can be used as follows:

if 1 > 2:
    print("1 is bigger than 2")

elif 2 > 1:
    print("2 is bigger than 1")

else:
    print("2 is equal to 1")


# In Python, the part after an "if" is called an expression
# if there's no explicit expression, Python's interpreter will cast the second part to a boolean value
if True:
    print("It's True")

else:
    print("It's False")


# To negate an expression, Python uses "not":
x = None
if x is not None:
    print("x was not Null!")

# When checking if a variable has a true value, just use the variable name with no operator:
# (false values are: empty strings (""), 0 and None)
if x:
    print("x has a true value")

else:
    print("x has a false value")


# We can combine multiple expressions, and unlike other programming languages, parenthesis are useful but not required:
x = 5
if x > 0 and x < 10:  # can be written as `if (x > 0 and x < 10):` as well
    print("x between 0 and 10")

# For the above example, checking if x is between two numbers, the following statement is recommended instead:
if 0 < x < 10:
    print("x between 0 and 10")



