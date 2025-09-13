#Then, in a file called test_fuel.py, implement two or more functions that collectively test your
#  implementations of convert and gauge thoroughly, each of whose names should begin with test_ so
#  that you can execute your tests with:

import pytest
from fuel import convert, gauge

# ---------- Tests for convert ----------

def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/100") == 1
    assert convert("99/100") == 99

def test_convert_rounding():
    assert convert("1/3") == 33   # 0.333... → 33
    assert convert("2/3") == 67   # 0.666... → 67

def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("cat/dog")   # not integers
    with pytest.raises(ValueError):
        convert("2/1")       # X > Y
    with pytest.raises(ZeroDivisionError):
        convert("1/0")       # Y = 0


# ---------- Tests for gauge ----------

def test_gauge_edges():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_middle():
    assert gauge(50) == "50%"
    assert gauge(67) == "67%"