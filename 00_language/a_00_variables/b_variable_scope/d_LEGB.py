# LEGB rule: Local, Enclosing, Global, Built-in.

the_variable = 'This is the global variable'


def which():
    print(the_variable)


def child_which():
    the_variable = 'This is the enclosing variable'

    def which():
        print(the_variable)

    which()


def grand_child_which():
    the_variable = 'This is the parent enclosing variable'

    def which():
        def which():
            print(the_variable)

        which()

    which()


if __name__ == '__main__':

    which()
    child_which()
    grand_child_which()
