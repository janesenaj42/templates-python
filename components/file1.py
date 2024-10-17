import logging.config

logger = logging.getLogger('customLogger')


def print_logs():
    logger.debug("This is file1 debug.")
    logger.info("This is file1 info.")
    logger.warning("This is file1 warn.")
    logger.error("This is file1 error.")
    logger.critical("This is file1 critical.")