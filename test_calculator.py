import pytest
from calculator import add, subtract, multiply, divide


# ===== اختبارات الجمع =====
def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 0) == 0


# ===== اختبارات الطرح =====
def test_subtract_positive():
    assert subtract(10, 4) == 6

def test_subtract_negative():
    assert subtract(-5, -3) == -2


# ===== اختبارات الضرب =====
def test_multiply_positive():
    assert multiply(3, 4) == 12

def test_multiply_by_zero():
    assert multiply(5, 0) == 0


# ===== اختبارات القسمة =====
def test_divide_positive():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
