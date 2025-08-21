"""Configuration settings for ms_demo_project."""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from top-level of your project
dotenv_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path)

class Config:
    """Central configuration class."""
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
    DISABLE_LOGGING = os.getenv("DISABLE_LOGGING", "False").lower() in ("true", "1", "yes")

# Create a global config instance
config = Config()
