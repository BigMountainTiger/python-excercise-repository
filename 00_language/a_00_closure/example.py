def get_funcs():

    the_variable = None

    def set_variable(v):
        nonlocal the_variable
        the_variable = v

    def get_variable():
        return the_variable

    return set_variable, get_variable


def run():
    set_variable, get_variable = get_funcs()

    set_variable(100)
    print(f'The variable is set to "{get_variable()}"')

    set_variable('OK')
    print(f'The variable is set to "{get_variable()}"')


if __name__ == '__main__':
    run()
