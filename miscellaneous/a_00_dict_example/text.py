
def test_keys():
    d = {
        'A': 'This is A',
        'B': 'This is B'
    }

    keys = d.keys()
    if 'A' in keys:
        print('A is in the keys')

    if not ('C' in keys):
        print('C is not in the keys')


if __name__ == '__main__':
    test_keys()
