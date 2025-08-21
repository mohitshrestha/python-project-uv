# shared/utils/math/arithmetic.py
"""Math arithmetic utilities"""

def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Divide a by b. Returns float('inf') if b is zero."""
    if b == 0:
        return float('inf')  # or 0
    return a / b

def modulus(a: float, b: float) -> float:
    """Return the remainder of a divided by b. Returns 0 if b is zero."""
    if b == 0:
        return 0
    return a % b

def exponent(a: float, b: float) -> float:
    """Return a raised to the power of b."""
    return a ** b

def floor_divide(a: float, b: float) -> float:
    """Perform floor division of a by b. Returns 0 if dividing by zero."""
    if b == 0:
        return 0  # safe default
    return a // b
