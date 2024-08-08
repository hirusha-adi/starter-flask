# Imports
import logging
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

import colorlog

from app.config import Other


# log format
log_format = (
    "%(asctime)s | %(levelname)s | %(filename)s:%(funcName)s:%(lineno)d - %(message)s"
)
log_datefmt = "%Y-%m-%d %H:%M:%S"

# colorlog
formatter = colorlog.ColoredFormatter(
    "%(log_color)s" + log_format,
    datefmt=log_datefmt,
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "red,bg_white",
    },
)

# console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# configure root logger (console handler)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)

# add logging to file
if str(Other.LOG_TO_FILE).strip().lower() == "true":
    # log into ./logs foler
    log_directory = "./logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Save to a new file every day
    # https://stackoverflow.com/a/59762352
    log_filename = datetime.now().strftime("%Y-%m-%d.log")

    file_handler = TimedRotatingFileHandler(
        os.path.join(log_directory, log_filename),
        when="midnight",
        interval=1,  # per each dat
        backupCount=15,  # keep up to 15 days of logs
    )

    file_handler.suffix = "%Y-%m-%d"
    file_handler.setFormatter(logging.Formatter(log_format, datefmt=log_datefmt))

    logger.addHandler(file_handler)