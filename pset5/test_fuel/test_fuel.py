from fuel import convert, gauge
from pytest import raises

def test_convert_valid_faction():
    assert convert("3/4") == 75


def test_convert_zero_division():
    with raises(ZeroDivisionError):
        convert("100/0")


def test_convert_larger_numerator():
    with raises(ValueError):
        convert("4/3")


def test_convert_non_number():
    with raises(ValueError):
        convert("cat")

def test_gauge_percentage():
    assert gauge(50) == "50%"


def test_gauge_empty():
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"