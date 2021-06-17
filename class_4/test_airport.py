#!/usr/bin/env python3
# coding: utf-8
"""Contains tests for all airport Classes"""

import pytest
from aircraft import AirbusA319, Boeing777
from flight import Flight
from passenger import Passenger


def test_airbus():
    a = AirbusA319("XXXXX")
    assert a is not None
    assert a.model() == "Airbus A319"
    assert len(a.list_seats()) == 132


def test_flight():
    a = AirbusA319("XXXXX")
    f = Flight("TT1111", a)

    with pytest.raises(ValueError):
        f2 = Flight("XXXX", a)
