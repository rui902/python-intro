#!/usr/bin/env python3
# coding: utf-8
"""Contains printer functions for flight tickets"""


def ticket_printer(passenger_name, seat, flight_number, aircraft_model):
    """Prints a ticket in the 'a' format in the console

    Attrs:
        passenger: passenger name
        seat: seat identifier
        flight_number: flight number code
        aircraft: aircraft model

    :returns: None
    """

    output = f"| Name: {passenger_name}" \
             f"  Flight: {flight_number}" \
             f"  Seat: {seat}" \
             f"  Aircraft: {aircraft_model}" \
             f" |"
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"

    ticket = "\n".join([banner, border, output, border, banner])
    print(ticket)
    print()


if __name__ == "__main__":
    help(ticket_printer)

    ticket_printer("Rui Costa", "1A", "TP1242", "Airbus 369")
