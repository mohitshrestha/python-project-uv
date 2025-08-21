"""Logger setup for ms_demo_project."""
import logging
from ms_demo_project.config import config
from rich.logging import RichHandler

def get_logger(name: str) -> logging.Logger:
    """
    Returns a configured logger.
    
    Logging can be completely disabled via DISABLE_LOGGING env variable.
    Logging level is controlled via LOG_LEVEL.
    """
    if config.DISABLE_LOGGING:
        logging.disable(logging.CRITICAL)  # Suppress all logging
        logger = logging.getLogger(name)
        logger.addHandler(logging.NullHandler())
        return logger

    logging.basicConfig(
        level=logging.DEBUG if config.DEBUG else getattr(logging, config.LOG_LEVEL, logging.INFO),
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)]
    )

    return logging.getLogger(name)
