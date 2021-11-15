
# parent
class parent():

    def __init__(self):
        self.state = 'OPEN'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.state = 'CLOSED'
        print('exit method called')


class child(parent):

    def __init__(self):
        super().__init__()

    def print(self):
        print(self.state)

    def raise_exception(self):
        raise Exception('Raise an exeption in context manager')


def test():
    try:
        with child() as obj:
            obj.print()
            obj.raise_exception()
    except Exception as e:
        print(str(e))

    obj.print()

    with child() as obj:
        obj.print()
        print('The exit method will be called with/without an exception')
        print()
        obj.raise_exception()

    obj.print()


if __name__ == '__main__':
    test()
