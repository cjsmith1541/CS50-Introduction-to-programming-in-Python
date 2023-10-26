from cs50p.pset5.test_bank.bank import value

def test_hello():
    assert value("hello, world") == 0


def test_h_start():
    assert value("help, me") == 20


def test_no_greeting():
    assert value("shutup") == 100


def test_case_insensitivity():
    assert value("HELLO, world") == 0