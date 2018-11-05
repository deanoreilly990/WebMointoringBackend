#process and construct the data into a JSON format
# Wait for the API calls - send back JSON object --

import logging
from logging.config import fileConfig

import backend


def main():
    fileConfig('logging_config.ini')
    logger = logging.getLogger()
    backend.getLocalCPUlevels()


main()
