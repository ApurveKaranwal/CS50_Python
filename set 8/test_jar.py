import pytest
from jar import Jar

def test_initialization():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5

def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2

def test_overfill():
    jar = Jar(10)
    jar.deposit(10)
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_underfill():
    jar = Jar(10)
    with pytest.raises(ValueError):
        jar.withdraw(1)
