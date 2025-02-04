"""
This module contains unit tests for the multiplication function in the app.mult module.
"""
from app.mult import mult

def test_multiplication():
    """Tests the multiplication function with various cases."""
    assert mult(3, 4) == 12
    assert mult(-2, 5) == -10
    assert mult(0, 100) == 0
