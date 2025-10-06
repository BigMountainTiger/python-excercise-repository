def run():
    print(the_variable)

    # IF a variable assigned, it it treated as a local variable
    # The following line will be a run-time error:
    # UnboundLocalError: cannot access local variable 'the_variable' where it is not associated with a value
    # the_variable = "What is this"


the_variable = 'The variable is declared after the function that uses it'


if __name__ == '__main__':
    run()