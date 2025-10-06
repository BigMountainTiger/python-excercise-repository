class a_class():
    def __init__(self):
        self.value = 'A value set to the object'

    def print_though_self(self):
        print(self.value)

    def print_though_not_self(not_self):
        # The referene is allowed to named to not "self"
        print(not_self.value)


if __name__ == '__main__':

    obj = a_class()

    obj.print_though_self()
    obj.print_though_not_self()

    print()
    print('Conclusion:')
    print('The instance reference can be named not "self"')
