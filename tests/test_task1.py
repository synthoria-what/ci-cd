from src.task1.main import is_int, is_prime, add, minus


def test_is_int():
    assert is_int("1") == False

def test_is_prime():
    assert is_prime(3) == False

def test_add():
    assert add(100, 2) == 102

def test_minus():
    assert minus(40, 1) == 39

def test_add_1():
    assert add(100, 10) != 100