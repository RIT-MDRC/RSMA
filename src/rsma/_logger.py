import logging
from datetime import datetime as d

import __main__

LOG_LEVEL = {
    "Debug": logging.DEBUG,
    "Info": logging.INFO,
    "Warning": logging.WARNING,
    "Error": logging.ERROR,
    "Critical": logging.CRITICAL,
}


def map_level(level: str) -> int:
    """
    Maps the level string to the corresponding logging level.

    :param level: the level string
    :return: the logging level
    """
    return LOG_LEVEL.get(level, logging.DEBUG)


def configure_logger(level: str = "Debug"):
    """
    Configure the logger.

    :param level: the level to log at
    """
    lvl = map_level(level)
    print(f"Configuring logger {level}...")
    start_time = d.now().strftime("%Y-%m-%d.%H:%M:%S")
    filename = "foundation." + __main__.__file__.split("/")[-1].split(".")[0]
    logging.basicConfig(
        filename=f".log/{start_time}.{filename}.{level}.log",
        format="foundation:%(filename)s: %(message)s",
        level=lvl,  # TODO: hook it to env or config file
        force=True,
    )
