from twttr import shorten

def test_correct_output():
    assert shorten("twitter") == 'twttr'

def test_capitalized():
    assert shorten("TWITTER") == 'TWTTR'

def test_numbers():
    assert shorten("twitter12345") == 'twttr12345'

def test_punctuation():
    assert shorten("twitter's!") == 'twttr\'s!'