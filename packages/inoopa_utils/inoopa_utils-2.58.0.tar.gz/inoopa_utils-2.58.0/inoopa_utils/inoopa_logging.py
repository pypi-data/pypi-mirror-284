"""Base Inoopa configuration for python Logging."""

from dotenv import load_dotenv

load_dotenv()
import os
import logging
from typing import Literal
from datetime import datetime
from rich.logging import RichHandler

from inoopa_utils.utils.env_variables_helper import get_env_name


LoggingLevel = Literal["CRITICAL", "FATAL", "ERROR", "WARN", "WARNING", "INFO", "DEBUG"]


def create_logger(
    logger_name: str, logging_level: LoggingLevel | None = None, logs_dir_path: str = "./logs", pretty: bool = False
) -> logging.Logger:
    """
    Configure how logging should be done.

    :param logger_name: The logger name to return.
    :param logging_level: The level of logging to filter. If none, will deduce from "ENV" env variable:
        'dev' will set logging_level to "DEBUG"
        'staging' will set logging_level to "INFO"
        'prod' will set logging_level to "INFO"
    :param logs_dir_path: The path to the logs directory.
    :param pretty: If True, will use rich to pretty print the logs. Only for development & CLI purpose.
    """

    # If the log directory doesn't exist, create it to avoid errors
    if not os.path.exists(logs_dir_path):
        os.makedirs(logs_dir_path, exist_ok=True)
        print(f"logs dir create at: {logs_dir_path}")

    if pretty:
        handlers = [RichHandler(rich_tracebacks=True, show_path=False, show_time=False, show_level=True)]
        log_format = "%(message)s"
    else:
        handlers = [
            # Write logs to file
            logging.FileHandler(f"{logs_dir_path}/{datetime.now().strftime('%d-%m-%Y_%H:%M')}.log"),
            # Allow the logger to also log in console
            logging.StreamHandler(),
        ]
        log_format = "%(asctime)s %(levelname)-8s %(name)-20s -> %(message)s"

    logging.basicConfig(
        # Define the log level for externals (libs) loggers
        level=logging.ERROR,
        handlers=handlers,
        format=log_format,
        datefmt="%d/%m/%Y %H:%M:%S",
    )

    if logging_level is None:
        logging_level = "DEBUG" if get_env_name() == "dev" else "INFO"

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging_level)
    return logger


if __name__ == "__main__":
    logger = create_logger("test_logger", logging_level="DEBUG", pretty=True)
    logger.info("test {'hello': 'world'}")
