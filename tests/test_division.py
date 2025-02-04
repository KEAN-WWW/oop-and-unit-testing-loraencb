"""
This module contains tests for the division function in the app.div module.
It includes tests for regular division and handling division by zero.
"""
import pytest
from app.div import div
def test_division():
    """Tests the division function with valid inputs."""
    assert div(10, 2) == 5
    assert div(9, 3) == 3

def test_divide_zero_exception():
    """Tests that division by zero raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        div(5, 0)
