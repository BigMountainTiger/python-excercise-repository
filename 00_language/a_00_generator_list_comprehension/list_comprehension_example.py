def run():
    x = 0

    lst = [x*x for x in range(10)]
    print(type(lst))
    print(lst)

    lst = [x for x in range(10) if x != 2]
    print(type(lst))
    print('2 is removed')
    print(lst)

    print()
    print('1. List comprehension create an actual list')
    print('2. List comprehension with if but no else remove entries from the list')
    print(
        f'3. List comprehension starts a new variable scope, the x remains = {x}')


if __name__ == '__main__':
    run()
