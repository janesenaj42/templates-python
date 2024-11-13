"""
Tests for main.py.
"""

from my_package.main import to_upper


def test_to_upper():
    """
    Test that to_upper() works.
    """
    assert to_upper("asdf") == "ASDF"
