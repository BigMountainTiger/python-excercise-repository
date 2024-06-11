class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def edit(e, x, y, payload):
    return {
        'e': e,
        'x': x,
        'y': y,
        'payload': payload
    }


def build_b(a, E):
    b = ''

    prev_x = 0
    for e in E:
        edit = e['e']
        x = e['x']
        y = e['y']
        payload = e['payload']

        for i in range(prev_x, x - 1 if edit == '-' else x):
            b = b + a[i]

        if edit == '+':
            b = b + payload

        prev_x = x

    for i in range(prev_x, len(a)):
        b = b + a[i]

    return b


def print_diff(S, E):
    a = S['a']
    b = S['b']

    prev_x = 0
    for e in E:
        edit = e['e']
        x = e['x']
        y = e['y']

        # the entry should be exclusive on a if deletion
        for i in range(prev_x, x - 1 if edit == '-' else x):
            print(a[i])

        text = f'{bcolors.FAIL}- {a[x - 1]}{bcolors.ENDC}' if edit == '-' else f'{
            bcolors.OKGREEN}+ {b[y - 1]}{bcolors.ENDC}'
        print(text)

        prev_x = x

    for i in range(prev_x, len(a)):
        print(a[i])
