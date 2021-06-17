#!/usr/bin/env python3
# coding: utf-8
"""Contains class definitions for Aircrafts"""


# class Aircraft:
#     """ An aircraft is defined as the passenger aircraft which varies in seating number and arrangement
#
#     Attrs:
#         _model: The aircraft model
#         _seats_per_row: The number of seats per each row
#         _num_rows: The total number of seat rows
#     """
#
#     _model = None
#     _num_rows = None
#     _seats_per_row = None
#
#     def __init__(self, model, num_seats, num_rows):
#         self._model = model
#         self._seats_per_row = num_seats
#         self._num_rows = num_rows
#
#     def model(self):
#         return self._model
#
#     def all_seats(self):
#         # Letters I and O skipped to avoid confusion with numbers 1 and 0
#         return range(1, self._num_rows + 1), "ABCDEFGHJKLMNPQRS"[:self._seats_per_row]
#
#     def list_seats(self):
#         rows, letters = self.all_seats()
#         return ["%s%s" % (r, l) for r in rows for l in letters]


class BaseAircraft:

    def registration(self):
        return self._registration


class AdvancedAircraft:

    def list_seats(self):
        rows, letters = self.all_seats()
        return ["%s%s" % (r, l) for r in rows for l in letters]


class AirbusA319(BaseAircraft, AdvancedAircraft):

    def __init__(self, registration):
        self._registration = registration

    def model(self):
        return "Airbus A319"

    def all_seats(self):
        return range(1, 23), "ABCDEF"


class Boeing777(BaseAircraft, AdvancedAircraft):

    def __init__(self, registration):
        self._registration = registration

    def model(self):
        return "Boeing 777"

    def all_seats(self):
        return range(1, 56), "ABCDEFGHJK"


if __name__ == "__main__":
    from pprint import pprint as pp

    # help(Aircraft)

    # ac = Aircraft("Airbus A396", num_rows=5, num_seats=5)

    # print("all_seats()")
    # pp(ac.all_seats())

    # print("\n")

    # print("list_seats()")
    # pp(ac.list_seats())

    a = AirbusA319("G-EUPT")
    b = Boeing777("F-GSPS")

    pp(a.registration())
    print(a.list_seats())

    print("\n")

    pp(b.registration())
    print(b.list_seats())
