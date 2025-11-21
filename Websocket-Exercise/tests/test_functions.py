# tests/test_functions.py
from myws.server import average


def test_average_with_integers():
    assert average(2, 4) == 3.0
    assert average(1, 1) == 1.0


def test_average_with_floats():
    assert average(2.5, 3.5) == 3.0
    assert average(-1.0, 1.0) == 0.0