
import pytest

from validators import validate_amount


def test_valid_amount():
    assert validate_amount("50") == 50.0


def test_amount_rounding():
    assert validate_amount("25.678") == 25.68


def test_negative_amount():
    with pytest.raises(ValueError):
        validate_amount("-10")


def test_zero_amount():
    with pytest.raises(ValueError):
        validate_amount("0")


def test_invalid_amount():
    with pytest.raises(ValueError):
        validate_amount("abc")
