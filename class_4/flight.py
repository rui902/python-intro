#!/usr/bin/env python3
# coding: utf-8
"""Contains class definitions for Flight"""

# from aircraft import Aircraft
from aircraft import AirbusA319, Boeing777
from passenger import Passenger


class Flight:
    """ A flight is defined as the identifier of a trip

    Attrs:
        _number: A flight number has two uppercase letters and 4 digits, e.g.: "TP1234"
        _aircraft: A flight has one passenger aircraft associated
        _seats: The seating plan for each passenger on the flight
    """

    _number = None
    _aircraft = None
    _seats = []

    def __init__(self, number, aircraft):
        Flight._validate_flight_number(number)

        self._number = number

        self._aircraft = aircraft

        rows, letters = self._aircraft.all_seats()
        self._seats = [None] + [{lt: None for lt in letters} for _ in rows]

    @staticmethod
    def _validate_flight_number(number):
        if not number[:2].isalpha():
            raise ValueError(f"No valid code provided in {number}")

        if not number[:2].isupper():
            raise ValueError(f"No valid airline code provided in {number}")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number: {number}")

        return True

    def number(self):
        return self._number

    def aircraft_model(self):
        # nunca se retorna um objeto para o user aceder, nós que temos conhecimento devemos retornar o necessário
        return self._aircraft.model()

    def seats(self):
        return self._seats

    def list_seats(self):
        return self._aircraft.list_seats()

    def _parse_seat(self, seat):
        """Parses a string containing a seat identifier returning the row number and letter

        :param seat: the string containing the seat ID
        :return: tuple(row, letter) that was parsed
        :raises: ValueError if argument is invalid
        """

        if not seat:
            raise ValueError("Seat cannot be empty")

        rows, letters = self._aircraft.all_seats()  # não é static por causa desta linha, mas podia ser

        letter = seat[-1]
        if letter not in letters:
            raise ValueError(f"Invalid Seat letter {letter}")

        row = seat[:-1]
        try:
            row = int(row)
        except ValueError:
            raise ValueError(f"Invalid Row number {row}")

        if row not in rows:
            raise ValueError(f"Invalid Seat Row {row}")

        return row, letter

    def assign_seat(self, seat, passenger):
        """Assigns a seat to a given passenger

        Args:
            seat: Seat identifier (number-letter)
            passenger: Passenger object

        Raises:
            ValueError: if the seat identifier is invalid or seat is already taken
        """

        row, letter = self._parse_seat(seat)

        if self._seats[row][letter]:
            raise ValueError(f"Seat {seat} is already taken!")

        self._seats[row][letter] = passenger

    def num_available_seats(self):
        return sum(sum(1 for seat in row.values() if seat is None) for row in self._seats if row is not None)

    def num_used_seats(self):
        return sum(sum(1 for seat in row.values() if seat is not None) for row in self._seats if row is not None)

    def make_boarding_tickets(self, ticket_printer=None):
        if not ticket_printer:
            raise Exception("No ticket printer selected")

        for passenger, seat in sorted(self._passenger_seats()):
            ticket_printer(passenger, seat, self._number, self.aircraft_model())

    def _passenger_seats(self):
        """Returns an iterable of tuples containing (passenger instance, seat id)"""

        rows, letters = self._aircraft.all_seats()

        for row in rows:
            for letter in letters:
                passenger = self._seats[row][letter]
                if passenger is not None:
                    yield (passenger.name(), f"{row}{letter}")


if __name__ == "__main__":
    from pprint import pprint as pp

    help(Flight)

    a = AirbusA319("G-EUPT")

    f1 = Flight("TP1234", aircraft=a)
    print("Flight 1 number: %s" % f1.number())

    print("Available Seats in Airbus:", f1.num_available_seats())

    p1 = Passenger("Rui Costa", "C123456")
    p2 = Passenger("Maria Rosário", "C234567")
    p3 = Passenger("Joaquim Alves", "C345678")

    print("Assigning passenger Seats")
    f1.assign_seat("1A", p1)
    f1.assign_seat("1B", p2)

    print("Available Seats in Airbus:", f1.num_available_seats())

    print("\n")

    from ticket_printer_a import ticket_printer

    print("Airbus Flight Tickets:")
    f1.make_boarding_tickets(ticket_printer)

    print("\n")

    b = Boeing777("F-GSPS")

    f2 = Flight("TP1698", aircraft=b)

    print("Flight 2 number: %s" % f2.number())

    print("Available Seats in Boeing:", f2.num_available_seats())

    print("Assigning passenger Seats")
    f2.assign_seat("5E", p3)

    print("Available Seats in Boeing:", f2.num_available_seats())

    print("Boeing Flight Tickets:")
    f2.make_boarding_tickets(ticket_printer)
