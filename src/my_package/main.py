"""
This is a sample code.
"""

import configparser
import logging.config
import os

import uvicorn
from fastapi import FastAPI

from my_package.components import file1, file2, file3

logging.config.fileConfig(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "logging.ini")
)

logger = logging.getLogger(__name__)


# Read config
config_file_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "..", "..", "config.ini"
)
config = configparser.ConfigParser(allow_no_value=True)
with open(config_file_path, "r", encoding="utf-8") as f:
    config.read_file(f)

SERVER_PORT = os.environ.get("SERVER_PORT", config.get("server", "port"))
SERVER_HOST = os.environ.get("SERVER_HOST", config.get("server", "host"))

app = FastAPI()


def to_upper(x: str) -> str:
    """
    Converts string to upper case.
    """
    return x.upper()


@app.get("/test")
def hello(name: str = ""):
    """
    Sample test endpoint.
    """
    return {"message": f"Hello {to_upper(name)}"}


if __name__ == "__main__":
    logger.debug("This is debug.")
    logger.info("This is info.")
    logger.warning("This is warn.")
    logger.error("This is error.")
    logger.critical("This is critical.")

    file1.print_logs()
    file2.print_logs()
    file3.print_logs()

    uvicorn.run(app, host=SERVER_HOST, port=int(SERVER_PORT))
