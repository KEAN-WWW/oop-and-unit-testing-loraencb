"""
This module contains unit tests for the subtraction function in the app.sub module.
"""
from app.sub import sub

def test_subtraction():
    """Tests the subtraction function with various cases."""
    assert sub(10, 5) == 5
    assert sub(0, 3) == -3
    assert sub(7, 7) == 0
