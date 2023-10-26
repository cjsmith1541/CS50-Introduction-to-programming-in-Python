from numb3rs import validate

def test_first_byte():
    assert validate("125.430.430.431") is False

def test_min():
    assert validate("0.0.0.0") is True

def test_max():
    assert validate("255.255.255.255") is True

def test_too_big():
    assert validate("512.512.512.512") is False

def test_too_many_digits():
    assert validate("1.2.3.10000") is False

def test_wrong_input():
    assert validate("cat") is False
