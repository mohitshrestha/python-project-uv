# tests/test_feature_string.py
from ms_demo_project.shared.utils.string.formatting import (
    to_upper, to_lower, to_title, to_snake, to_kebab, to_reverse
)

def test_to_upper():
    assert to_upper("hello world") == "HELLO WORLD"
    assert to_upper("") == ""

def test_to_lower():
    assert to_lower("HELLO WORLD") == "hello world"
    assert to_lower("") == ""

def test_to_title():
    assert to_title("hello world") == "Hello World"
    assert to_title("multiple words here") == "Multiple Words Here"

def test_to_snake():
    assert to_snake("Hello World") == "hello_world"
    assert to_snake("Multiple Words Here") == "multiple_words_here"

def test_to_kebab():
    assert to_kebab("Hello World") == "hello-world"
    assert to_kebab("Multiple Words Here") == "multiple-words-here"

def test_to_reverse():
    assert to_reverse("hello") == "olleh"
    assert to_reverse("") == ""
