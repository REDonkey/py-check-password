from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_password_without_uppercase() -> None:
    assert check_password("password@1") is False


def test_password_without_special_symbol() -> None:
    assert check_password("Password1") is False


def test_password_without_digit() -> None:
    assert check_password("Password@") is False


def test_password_too_short() -> None:
    assert check_password("P@ss1") is False


def test_password_too_long() -> None:
    assert check_password("Password@1234567890") is False
