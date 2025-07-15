import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def log_something():
    print(f'Current logging level = {logger.level}')
    logger.info('Info message')
    logger.debug('Info message')


if __name__ == '__main__':

    print('Use default logging level')
    log_something()

    print()
    print('Use logging.DEBUG logging level')
    logger.setLevel(logging.DEBUG)
    log_something()

    print()
    print('Use logging.INFO logging level')
    logger.setLevel(logging.INFO)
    log_something()

    print()
    print('Switch back to logging.DEBUG logging level')
    logger.setLevel(logging.DEBUG)
    log_something()

    print()
    print('Conclusion')
    print('1. It looks like the initial logging.basicConfig(level=logging.INFO) is necessary')
    print('2. Logging level can be changed at any time')
