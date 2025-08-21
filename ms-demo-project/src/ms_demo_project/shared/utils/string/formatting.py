# shared/utils/string/formatting.py

def to_upper(text: str) -> str:
    """Convert string to uppercase."""
    return text.upper()

def to_lower(text: str) -> str:
    """Convert string to lowercase."""
    return text.lower()

def to_title(text: str) -> str:
    """Convert string to title case."""
    return text.title()

def to_snake(text: str) -> str:
    """Convert string to snake_case."""
    return text.lower().replace(" ", "_")

def to_kebab(text: str) -> str:
    """Convert string to kebab-case."""
    return text.lower().replace(" ", "-")

def to_reverse(text: str) -> str:
    """Reverse the string."""
    return text[::-1]


