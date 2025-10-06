class example_class():
    def __init__(self):
        self.value = "This is the instance value"

    def _print_value(self):
        print(self.value)

    def __print_value(self):
        print(self.value)

    def access_private_method(self):
        self.__print_value()


if __name__ == '__main__':

    o = example_class()

    print('Single under_score is advisory private, but not enforced')
    o._print_value()

    print()
    print('Double under_score method, python change the method name to include the class name so making it harder to access')
    o._example_class__print_value()

    print()
    print('Double under_score method is accessed inside the class with no problem')
    o.access_private_method()
