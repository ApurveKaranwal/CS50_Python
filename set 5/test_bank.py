'''Then, in a file called test_bank.py, implement three or more functions that collectively 
test your implementation of value thoroughly, each of whose names should begin with test_ so 
that you can execute your tests with:'''

from bank import value

def test_Hello():
    assert value("Hello")==0

def test_hello():
    assert value("hello")==0

def test_Hey():
    assert value("Hey")==20

def test_h():
    assert value("hey")==20

def test_yo():
    assert value("yo")==100
