# The yield do not have to be the last line
def first_n(n):
    num = 0
    while num < n:
        yield num * num
        num += 1


def skip_even(n):
    num = 0
    while num < n:
        if num % 2 != 0:
            yield num

        num += 1


def run():
    x = 0

    generator_object = first_n(10)
    print(list(generator_object))
    print(list(generator_object))

    print('even numbers skipped')
    generator_object = skip_even(10)
    print(list(generator_object))

    print()
    print('1. A generator can be implemented as a fuc=nction')
    print('2. The list() function converts a generator object into a list')
    print('3. A generator object can be used only once')
    print('4. It is possible to conditionally "yield" to skip some entries')


if __name__ == '__main__':
    run()
