import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app")))

from main import check_password
import pytest

def test_valid_password():
    assert check_password("Pass@word1") is True

def test_too_short():
    assert check_password("P@ss1") is False

def test_too_long():
    assert check_password("Password@1234567890") is False

def test_no_uppercase():
    assert check_password("password@1") is False

def test_no_digit():
    assert check_password("Password@") is False

def test_no_special_char():
    assert check_password("Password1") is False

def test_invalid_char_space():
    assert check_password("Password 1@") is False

def test_invalid_char_percent():
    assert check_password("Password%1") is False

def test_boundary_min_length():
    assert check_password("A@bcdef1") is True

def test_boundary_max_length():
    assert check_password("Abcdef@123456789") is True

def test_non_latin_letters():
    assert check_password("Пароль@123") is False

@pytest.mark.parametrize("special", ["$", "@", "#", "&", "!", "-", "_"])
def test_each_allowed_special_char(special):
    password = f"Aa1{special}abcd"
    assert check_password(password) is True
