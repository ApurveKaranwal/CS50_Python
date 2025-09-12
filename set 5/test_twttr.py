'''In a file called test_twttr.py, implement one or more functions that collectively test your
 implementation of shorten thoroughly, each of whose names should begin with test_ so that you
  can execute your tests with:'''

from twttr import shorten

def test_lowercase():
    assert shorten("hello") == "hll"

def test_uppercase():
    assert shorten("HELLO") == "HLL"

def test_mixedcase():
    assert shorten("ApUrVe") == "prV"

def test_numbers():
    assert shorten("CS50") == "CS50"

def test_punctuation():
    assert shorten("CS50!!!") == "CS50!!!"
