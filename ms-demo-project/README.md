# ms-demo-project

A simple, modular, and scalable Python project template demonstrating:

- Modular structure with `features` and `shared/utils`
- Configurable logging with optional disable/debug mode
- Environment-based configuration via `.env`
- User input with defaults
- Arithmetic and string utilities with comprehensive tests
- Easy extensibility for adding new features

---

## Project Structure

```bash
ms-demo-project/
├─ data/
│ └─ credentials/ # Place your credentials here (optional)
├─ src/
│ └─ ms_demo_project/
│ ├─ features/
│ │ ├─ feature_math.py # Demonstrates arithmetic operations
│ │ └─ feature_string.py # Demonstrates string operations
│ ├─ shared/
│ │ └─ utils/
│ │ ├─ math/
│ │ │ └─ arithmetic.py # Arithmetic utilities
│ │ └─ string/
│ │ └─ formatting.py # String utilities
│ ├─ config.py # Configuration loader from .env
│ ├─ logger.py # Logger setup
│ └─ main.py # Entry point for the demo
├─ tests/
│ ├─ test_feature_math.py
│ └─ test_feature_string.py
├─ .env # Environment variables
├─ .env.sample # Sample env variables template
├─ pyproject.toml # pyproject config
└─ README.md # This file
```

---

## Getting Started

### 1. Install dependencies

```bash
uv pip install -r requirements.txt
```

# or if using uv:

```bash
uv install
```

## 2. Configure environment variables

Create a `.env` file at the project root (you can copy `.env.sample`):

```bash
# Enable debug mode (overrides LOG_LEVEL)
DEBUG=False

# Logging level: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL=INFO

# Disable all logging if True
DISABLE_LOGGING=False
```

`DEBUG` will override `LOG_LEVEL`.
`DISABLE_LOGGING=True` will completely suppress logs but main outputs are still displayed.

## 3. Run the demo

```bash
uv run python -m ms_demo_project.main
```

**Behavior**:

- Prompts the user for arithmetic values (defaults: `2` and `3`).
- Prompts the user for a string (default: `"hello world"`).
- Performs all arithmetic and string operations and displays results.
- Logs detailed info if logging is enabled.

## 4. Project Features

**Arithmetic** (`feature_math.py`):

- Addition, Subtraction, Multiplication, Division, Modulus, Exponent, Floor Division
- Handles invalid input and zero division safely

**String** (`feature_string.py`):

- Uppercase, Lowercase, Title Case, Snake Case, Kebab Case, Reverse
- Accepts user input or defaults

**Shared Utilities** (`shared/utils`):

- Keep reusable functions modular for maintainability
- `math/arithmetic.py` and `string/formatting.py` for demonstration

## 5. Logging

Configured in `logger.py` using `rich`:

```bash
from ms_demo_project.logger import get_logger
logger = get_logger(__name__)
```

Behavior controlled via `.env`:

- `DEBUG=True` → DEBUG-level logging
- `LOG_LEVEL=INFO` → Default logging level
- `DISABLE_LOGGING=True` → Logs completely suppressed

Even when logging is off, main demo prints results using `rich`.

## 6. Running Tests

All utilities are tested in `tests`/ using `pytest`.

```bash
uv run python -m pytest tests
```

- `test_feature_math.py` covers all arithmetic functions
- `test_feature_string.py` covers all string formatting functions
- Includes edge cases (e.g., division/modulus by zero, empty strings)

## 7. Extending the Template

- Add new features under `features/`
- Add reusable functions under `shared/utils/`
- Use `config.py` for any environment-based settings
- Use `logger.py` to consistently log in new modules
- Keep `main.py` minimal and delegate functionality to features

## 8. Notes & Best Practices

- Keep secrets out of source code (`data/credentials` or `.env`)
- Use `.env.sample` to document required environment variables
- Return results from features so main can display even if logging is off
- Modular design allows easy testing, scaling, and reuse
- Follow this structure for all new Python projects

## 9. Requirements

- Python >= `3.13`
- [uv](https://docs.astral.sh/uv/) for running modules (optional)
- `rich` for formatted printing and logging
- `pytest` for testing