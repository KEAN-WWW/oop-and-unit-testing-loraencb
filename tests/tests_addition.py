"""This module contains unit tests for the addition function in the app.add module."""
from app.add import add

def test_addition():
    """Tests the addition function with various cases."""
    assert add(10, 5) == 15
    assert add(0, 3) == 3
    assert add(7, -10) == -3
