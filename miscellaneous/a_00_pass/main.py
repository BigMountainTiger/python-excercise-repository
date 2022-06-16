def example(n):
    if n == 1:
        print('1 is passed in')
    elif n == 2:
        print('2 is passed in')
    else:
        pass

    print(f'Finished for {n}')
    print()


if __name__ == '__main__':
    example(1)
    example(2)
    example(3)

    print('pass .... it only pass the block itself, not the outer block')