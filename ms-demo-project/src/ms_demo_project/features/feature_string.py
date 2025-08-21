# ms-demo-project/features/feature_string.py
from ms_demo_project.logger import get_logger
from ms_demo_project.shared.utils.string.formatting import (
    to_upper, to_lower, to_title, to_snake, to_kebab, to_reverse
)

logger = get_logger(__name__)

def get_input_string(prompt: str, default: str) -> str:
    """Prompt user for a string. Use default if input is empty."""
    user_input = input(f"{prompt} (default '{default}'): ")
    if not user_input.strip():
        print(f"No input provided. Using default value '{default}'.")
        return default
    return user_input

def demo_string_operations():
    """
    Demonstrates simple string operations using shared utils:
    - Uppercase
    - Lowercase
    - Title Case
    - snake_case
    - kebab-case
    - Reverse

    Prompts user for a string with a default value.

    Returns:
        dict: Dictionary containing original, reversed, uppercase, lowercase,
              title, snake_case, and kebab-case strings.
    """
    s = get_input_string("Enter a string", "hello world")

    results = {
        "original": s,
        "uppercase": to_upper(s),
        "lowercase": to_lower(s),
        "title": to_title(s),
        "snake_case": to_snake(s),
        "kebab_case": to_kebab(s),
        "reversed": to_reverse(s)

    }

    # Log results
    for key, value in results.items():
        logger.info(f"{key.replace('_', ' ').capitalize()}: {value}")

    return results
