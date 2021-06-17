#!/usr/bin/env python3
# coding: utf-8
"""Contains class definitions for Aircraft, Airport, Flight, Trip"""

class Aircraft:
    """ An aircraft is defined as the passenger aircraft which varies in seating number and arrangement

    Attrs:
        _model: The aircraft model
        _seats_per_row: The number of seats per each row
        _num_rows: The total number of seat rows
    """

    _model = None
    _num_rows = None
    _seats_per_row = None

    def __init__(self, model, num_seats, num_rows):
        self._model = model
        self._seats_per_row = num_seats
        self._num_rows = num_rows

    def model(self):
        return self._model

    def all_seats(self):
        # Letters I and O skipped to avoid confusion with numbers 1 and 0
        return range(1, self._num_rows + 1), "ABCDEFGHJKLMNPQRS"[:self._seats_per_row]

    def list_seats(self):
        rows, letters = self.all_seats()
        return ["%s%s" % (r, l) for r in rows for l in letters]


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

    # help(Aircraft)

    ac = Aircraft("Airbus A396", num_rows=5, num_seats=5)
    # print(ac.all_seats())
    # pp(ac.list_seats())

    help(Flight)

    f = Flight("TP1234", aircraft=ac)
    print("Flight number: %s" % f.number())

    print("Available Seats:", f.num_available_seats())
    print("Default Seats:")
    pp(f.seats())

    # help(Passenger)

    p1 = Passenger("Rui Costa", "C123456")
    p2 = Passenger("Maria Rosário", "C234567")
    p3 = Passenger("Joaquim Alves", "C345678")

    f.assign_seat("1A", p1)
    f.assign_seat("1B", p2)
    f.assign_seat("5E", p3)
    print("Seats after assigning new passenger:")
    pp(f.seats())
    print("Available Seats:", f.num_available_seats())

    # f.assign_seat("19C", p1)
    # f.assign_seat("1Z", p1)
    # f.assign_seat("AA", p1)

    # TPC:
    # Create a method that lists a list of tuples containg all available seats next to each other (e.g. [(1A, 1B), (1B, 1C)]
