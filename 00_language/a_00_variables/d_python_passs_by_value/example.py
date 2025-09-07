# Python variable is passed by value
def passing_by_value():
    print('passing_by_value()')

    def add(i):
        i += 1
        print(f'Increment in function - i = {i}')

    i = 0
    add(i)

    print(f'The variable remains the same in the calling function - i = {i}')
    print(f'Variables are passed by value')
    print()

if __name__ == '__main__':
  passing_by_value()