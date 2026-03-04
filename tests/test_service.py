# tests/test_service.py
from proj1.service import add_two_numbers

def test_add_positive():
    assert add_two_numbers(2, 3) == 5

def test_add_negative():
    assert add_two_numbers(-1, -1) == -2
