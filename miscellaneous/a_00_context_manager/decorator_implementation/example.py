from contextlib import contextmanager

# reference -
# https://docs.python.org/3/library/contextlib.html


@contextmanager
def example():
    try:

        print('setting up')
        yield "Anthing can be yield from here"
    finally:
        # The try/finally block is required for the tear down to happen if exception raised
        print('tearing down')


if __name__ == '__main__':

    with example() as txt:
        print(txt)
