import pytest
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def test_prime():
    assert is_prime(7) is True
def test_nonprime():
    assert is_prime(10) is False