def run():
    print(lazy_variable)
    lazy_function()


lazy_variable = 'This is the lazy variable'


def lazy_function():
    print('The lazy_function is called')


if __name__ == '__main__':
    run()

    print()
    print('1. In a function, it is OK to reference variable and function defined after the function')
    print('2. But the referenced variable or function must have been defined before the function is invoked')
