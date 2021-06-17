#!/usr/bin/env python3
# coding: utf-8
"""Contains class definitions for Passenger"""


class Passenger:
    """Passengers of a flight"""

    _name = None
    _passport = None

    def __init__(self, name, passport):
        self._name = name
        self._passport = passport

    def name(self):
        return self._name

    def passport(self):
        return self._passport

    def __repr__(self):
        return f"Passenger: {self._name} ({self._passport})"


if __name__ == "__main__":
    from pprint import pprint as pp

    help(Passenger)

    p1 = Passenger("Rui Costa", "C123456")
    pp(p1)