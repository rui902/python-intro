#!/usr/bin/env python3
# coding: utf-8
"""Imports the calculator script and calls multiple methods"""


# Another way of importing specific parts from a script
from calculator import add, sub, mul, div


def main():
    """Tests a few calculator function calls"""

    adds_1_2 = add(1, 2)
    print("adds 1 + 2:", adds_1_2)

    subtracts_1_2 = sub(1, 2)
    print("subtracts 1 - 2:", subtracts_1_2)

    multiplies_1_2 = mul(1, 2)
    print("multiplies 1 * 2:", multiplies_1_2)

    divides_1_2 = div(1, 2)
    print("divides 1 * 2:", divides_1_2)


print("I'm executing a random print call...")

if __name__ == "__main__":
    print("This is a very 'controlled' print call!")
    main()







