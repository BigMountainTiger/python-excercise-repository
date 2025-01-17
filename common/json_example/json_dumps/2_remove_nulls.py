import json


class NullEncoder(json.JSONEncoder):
    def default(self, obj):
        if obj is None:
            return None
        return json.JSONEncoder.default(self, obj)


def use_encoder():
    data = {'a': 1, 'b': None, 'c': 3}
    json_string = json.dumps(data, cls=NullEncoder)
    print(json_string)


def use_filter():

    data = {'a': 1, 'b': None, 'c': 3}
    filtered_data = {k: v for k, v in data.items() if v is not None}

    json_string = json.dumps(filtered_data)
    print(json_string)


if __name__ == '__main__':
    print('Use encoder')
    use_encoder()
    print('Note')
    print('1. It looks like using encoder does not work')
    print()

    print('Use filter')
    use_filter()
    print('Note')
    print('1. To remove the null entries, we can filter the dictionary')
