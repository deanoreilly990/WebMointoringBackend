#process and construct the data into a JSON format
# Wait for the API calls - send back JSON object --

def logger_Global():
    import logging
    logging.basicConfig(filename='logging.log', level=logging.DEBUG)
    logger = logging.getLogger()
    return logger

def main():
    import backend
    logger = logger_Global()
    logger.debug('Controller - Main Invoked - 200')
    backend.getLocalCPUlevels()
    print 'Main - ok'


def users():
    import backend
    return backend.return_root_log()

if __name__ == '__main__':
    main()
