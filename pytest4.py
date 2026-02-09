import pytest
def is_even(n):
    return n%2==0
def test_even():
    assert is_even(4) is True
def test_odd():
    assert is_even(5) is False