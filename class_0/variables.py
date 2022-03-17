#!/usr/bin/env python3
# coding: utf-8
"""Introduction to Python"""


# Python Variables
# A variable is programmable and can have multiple values during the execution of the script
# Python variables can have any name we want, with these exceptions: https://realpython.com/lessons/reserved-keywords/
# Python uses the snake_case style for variable names: https://en.wikipedia.org/wiki/Snake_case


# Text values (strings)
# In many programming languages, to represent strings, we use single or double quotes
# In Python, both are valid, as long as we use them consistently
# If we start using a single quote, we have to "close" the string with a single quote;
# If we start using a double quote, we have to "close" the string with a double quote
using_single_quotes = 'Single quotes are cool'
using_double_quotes = "Double quotes are fine as well!"

# We can use print(expression) to show the values of an expression/variable
print(using_single_quotes)
print(using_double_quotes)


# Numeric variables
number = 7
float_number = 4.20

# The following will round 4.20 to 4
rounded_number = int(float_number)
print(rounded_number)

# using int(variable) rounds towards 0, e.g.:
int(4.99)  # = 4
int(-4.99)  # = -4

# Using float(variable) we can cast/convert a string/int variable into a floating point number
float_from_int = float(4)  # 4.0
float_from_string = float("4.5")  # 4.5


# More on text variables
# For line breaks, we use the \n symbol
multi_line_in_one_line = "This is the first line\nThis is the second line!"

# We can see the following shows the above string in two lines as expected
print("multi_line_in_one_line:")
print(multi_line_in_one_line)

# We can also use multi-line strings using triple quotes, as follows:
multi_line_single_quoted = '''This is the line #1
This is the line #2
This is the line #3'''
print("multi_line_single_quoted:")
print(multi_line_single_quoted)

multi_line_double_quoted = """This is the line #1
This is the line #2
This is the line #3"""
print("multi_line_double_quoted:")
print(multi_line_double_quoted)


# Boolean values
# In programming, boolean values are very similar across languages, in Python we have:
# True
# False
# Note that True and False are case-sensitive, lowercase true/false is not recognized and will throw an exception
true_value = True


# Null values in Python
# Unlike many other languages, Python uses "None" to define Null values (note: None is also case-sensitive!)
null_value = None
false_value = False

# In Python, besides False, empty strings (""), 0 and None are also considered "falsy" values
# All other values are considered to be true values
# Keep it in mind, this will be explained in later classes!
