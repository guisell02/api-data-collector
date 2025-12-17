import logging


def setup_logger() -> logging.Logger:
    """Configure application logger."""
    logger = logging.getLogger("api_data_collector")
    logger.setLevel(logging.INFO)
    return logger
