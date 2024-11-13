"""
This is a sample file to test out logging functionalities.
"""

import logging.config

logger = logging.getLogger(__name__)


def print_logs():
    """
    Prints logs of different severity levels.
    """
    logger.debug("This is file3 debug.")
    logger.info("This is file3 info.")
    logger.warning("This is file3 warn.")
    logger.error("This is file3 error.")
    logger.critical("This is file3 critical.")
