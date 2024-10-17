import logging.config
from components import file1, file2, file3

logging.config.fileConfig('logging.ini')

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logger.debug("This is debug.")
    logger.info("This is info.")
    logger.warning("This is warn.")
    logger.error("This is error.")
    logger.critical("This is critical.")

    file1.print_logs()
    file2.print_logs()
    file3.print_logs()


    # docker pull python:3.11.10-slim-bookworm
    