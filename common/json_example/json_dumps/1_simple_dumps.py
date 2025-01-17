import json

template = {
    'B': None,
    'A': None
}


def run():
    data = template.copy()
    data['A'] = 'Value of A'
    str = json.dumps(data)
    print(str)

    data = template.copy()
    data['B'] = 'Value of B'
    str = json.dumps(data, sort_keys=True)
    print(str)

    print()
    print('Note:')
    print('1. By default json.dumps() keeps the null value entries')
    print('2. Set sort_keys=True will sort the keys of the json string')


if __name__ == '__main__':
    run()


