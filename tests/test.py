from src.math import add, subtract

def test_add():
    assert add(1,2) == 3
    assert add(2,2) == 4

def test_subtract():
    assert subtract(1,2) == -1 
    assert subtract(2,2) == 0