import logging

# DEBUG (10): Detailed information, typically used for diagnosing problems.
# INFO (20): General information about the program's execution, confirming that things are working as expected.
# WARNING (30): Indicates potential issues or unexpected events that might cause problems in the future.
# ERROR (40): Signals that a specific function or operation has failed, but the program can usually continue.
# CRITICAL (50): Represents severe errors that may lead to the program's termination. 
# NOTSET (0): When set, all levels will be logged.

if __name__ == '__main__':

    print(f'NOTSET - {logging.NOTSET}')
    print(f'DEBUG - {logging.DEBUG}')
    print(f'INFO - {logging.INFO}')
    print(f'WARNING - {logging.WARNING}')
    print(f'ERROR - {logging.ERROR}')
    print(f'CRITICAL - {logging.CRITICAL}')

    print()
    print('Only the logs above the set logging level will take effect')