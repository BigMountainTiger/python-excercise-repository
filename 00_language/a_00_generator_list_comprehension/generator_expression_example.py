def run():
    x = 0

    generator_object = (x*x for x in range(10))
    print(list(generator_object))
    print(list(generator_object))

    print()
    generator_object = (x for x in range(10) if x != 2)
    print('2 is removed')
    print(list(generator_object))

    print()
    print('1. A generator expression has similar syntax as list comprehension')
    print('2. The list() function converts a generator object into a list')
    print(
        f'3. A generator expression starts a new variable scope, the x remains = {x}')
    print('4. A generator object can be used only once')
    print('5. A generator object with if but no else removes entries from the generator')


if __name__ == '__main__':
    run()
