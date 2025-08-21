# ms-demo-project/features/feature_math.py
from ms_demo_project.logger import get_logger
from ms_demo_project.shared.utils.math.arithmetic import (
    add, subtract, multiply, divide, modulus, exponent, floor_divide
)

logger = get_logger(__name__)

def get_input_number(prompt: str, default: float) -> float:
    """Prompt user for a number. Use default if input invalid or empty."""
    user_input = input(f"{prompt} (default {default}): ").strip()
    try:
        return float(user_input) if user_input else default
    except ValueError:
        print(f"Invalid input. Using default value {default}.")
        return default

def demo_math_operations():
    """
    Demonstrates arithmetic operations using shared utils.
    Prompts user for two numbers with defaults.
    """
    a = get_input_number("Enter first value", 2)
    b = get_input_number("Enter second value", 3)

    results = {
        "first value": a,
        "second value": b,
        "add": add(a, b),
        "subtract": subtract(a, b),
        "multiply": multiply(a, b),
        "divide": divide(a, b) if b != 0 else "undefined",
        "modulus": modulus(a, b) if b != 0 else "undefined",
        "exponent": exponent(a, b),
        "floor_divide": floor_divide(a, b) if b != 0 else "undefined"
    }

    # Log results
    for op, val in results.items():
        logger.info(f"{op.replace('_', ' ').capitalize()}: {val}")

    return results
