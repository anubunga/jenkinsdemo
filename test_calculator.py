import pytest
import calculator

def test_add():
    assert calculator.add(2, 2) == 4
def test_subtract():
    assert calculator.subtract(10, 1) == 9
def test_multiply():
    assert calculator.multiply(7, 8) == 56
def test_divide():
    assert calculator.divide(24, 4) == 6