import pytest
from password import *

"""
Validates a password based on:
- Minimum length of 8
- At least one uppercase letter
- At least one lowercase letter
- At least one special character
Returns True if valid, otherwise raises ValueError.
"""

def test_password1():
    assert check_password("Password!") == True

def test_noSpecChar():
    with pytest.raises(ValueError):
        check_password("Password")

def test_noUpper():
    with pytest.raises(ValueError):
        check_password("password!")

def test_noLower():
    with pytest.raises(ValueError):
        check_password("PASSWORD!")

def test_lt8():
    with pytest.raises(ValueError):
        check_password("Passwd!")