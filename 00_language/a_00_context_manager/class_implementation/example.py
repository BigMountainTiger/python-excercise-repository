
class example():
    def __init__(self):
        pass

    def __enter__(self):
        # The critical resource should be created here, not the constructor
        print('setting up')

        # The __exit__() WILL NOT be called if an exception raised before this 'return'
        return 'Anything can be returned from here'

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('tearing down')


if __name__ == '__main__':

    with example() as txt:
        print(txt)
        # raise Exception('OK')
