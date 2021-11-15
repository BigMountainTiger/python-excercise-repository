
# parent
class parent():

    def __init__(self):
        self.state = 'OPEN'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.state = 'CLOSED'
        self.__close__()
        print('exit method called')

    def __close__(self):
        print('Parent Close')


class child(parent):

    def __init__(self):
        super().__init__()

    # Although called in the parent class in the __exit__ function
    # the child implementation is executed. 
    def __close__(self):
        print('Child Close')

    def print(self):
        print(self.state)

    def raise_exception(self):
        raise Exception('Raise an exeption in context manager')


def test():

    help(child)
    # Method resolution order - https://www.python.org/download/releases/2.3/mro/
    # Method override, so the child class __close__ method is called
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
