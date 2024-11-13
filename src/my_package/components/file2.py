"""
This is a sample file to test out logging functionalities.
"""

import logging.config

logger = logging.getLogger()


def print_logs():
    """
    Prints logs of different severity levels.
    """
    logger.debug("This is file2 debug.")
    logger.info("This is file2 info.")
    logger.warning("This is file2 warn.")
    logger.error("This is file2 error.")
    logger.critical("This is file2 critical.")
