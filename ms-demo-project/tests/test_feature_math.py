# tests/test_feature_math.py
import pytest
from ms_demo_project.shared.utils.math.arithmetic import (
    add, subtract, multiply, divide, modulus, exponent, floor_divide
)

def test_add():
    assert add(5, 3) == 8
    assert add(-2, 2) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2

def test_multiply():
    assert multiply(5, 3) == 15
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 0) == float('inf')  # safe default for zero division

def test_modulus():
    assert modulus(5, 2) == 1
    assert modulus(5, 0) == 0  # safe default for zero division

def test_exponent():
    assert exponent(2, 3) == 8
    assert exponent(5, 0) == 1

def test_floor_divide():
    assert floor_divide(7, 2) == 3
    assert floor_divide(7, 0) == 0  # safe default for zero division
