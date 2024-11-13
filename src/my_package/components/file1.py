"""
This is a sample file to test out logging functionalities.
"""

import logging.config

logger = logging.getLogger("customLogger")


def print_logs():
    """
    Prints logs of different severity levels.
    """
    logger.debug("This is file1 debug.")
    logger.info("This is file1 info.")
    logger.warning("This is file1 warn.")
    logger.error("This is file1 error.")
    logger.critical("This is file1 critical.")
