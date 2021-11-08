global v
v = 'This is the globally defined variable'


def func_1():
    v = 'Assigned in Func_1'
    print(v)


def func_2():
    global v
    v = 'Assigned in Func_2'
    print(v)


def run():
    func_1()
    print(v)

    print()
    func_2()
    print(v)

    print()
    print('The global keyword only takes effect when it is used inside of a function')


if __name__ == '__main__':
    run()
