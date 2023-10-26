from plates import is_valid

def test_vaild_plate():
    assert is_valid("CS50") is True


def test_start_letters():
    assert is_valid("50CS") is False


def test_letters_after_numbers():
    assert is_valid("CS50P") is False


def test_punctuation():
    assert is_valid("CS.50!") is False


def test_too_long():
    assert is_valid("HELLOWORLD2") is False


def test_too_short():
    assert is_valid("H") is False


def test_zero_placement():
    assert is_valid("CS05") is False

def test_all_numbers():
    assert is_valid("49568") is False