#!/usr/bin/env python3
# coding: utf-8
"""Introduction to Functional Programming in Python"""


# Defining functions
# Prototyping usually uses a `pass` keyword for an empty body
# Equivalent of "doing nothing"
def our_first_function():
    pass


# This function is called `print_some_variable`, receives a parameter called `parameter` and prints it in the screen
def print_some_variable(parameter):
    print(parameter)


# We create some random variable, in this cased it's called argument
# In a way, think of argument as the value that is sent to the function when calling it
# Parameters are just the "function variables"
argument = "My name is Rui"

# Call the function and print the above variable's value


# A little more complex function
# The following syntax for the p2 parameter is called a default value,
# meaning that when calling this function, it's not required to pass a second argument,
# and the p2 value will be assigned to "default"
def little_complex_function(p1, p2="default"):
    if p2 == "default":
        print("Value of p1:", p1)
        print("p2 has default value!")
    else:
        print("Value of p1:", p1)
        print("Value of p2:", p2)


# Calling a function doesn't require us to pass a variable, we can pass values directly as well!
little_complex_function("ABC", "DEF")

# Call the function without second argument
little_complex_function("ZZZ")

# The order of the arguments doesn't matter if we used the named argument notation
little_complex_function(p2="This is p2", p1="This is p1")


# Complex parameters:
# Parameters, by default, are positional, and they are called "formal parameters"
# There's a way to allow for dynamic argument passing, usually referenced as args and kwargs
def complex_params(p1, p2, *args, **kwargs):
    print("Value of p1:", p1)
    print("Value of p2:", p2)
    print("*args:", args)
    print("**kwargs:", kwargs)


# Calling while passing only p1 and p2
complex_params(1, 2)

# Calling while adding indefinite amount of unnamed args
complex_params(1, 2, 3, 4, 5)

# Calling while adding named keyword arguments
complex_params(1, 2, p3=3, p4=4, p5=5)


