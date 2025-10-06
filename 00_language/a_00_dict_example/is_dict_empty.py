def is_dict_empty(data):

    # This function only takes input of dict type. Exception is thrown if input of other types is passed in
    # 
    # A dict is considered not empty
    # 1. Any top level non-list type property is not None
    # 2. Any top level list type propery is not empty
    #
    # A None dict is considered empty

    if (data is not None) and (not isinstance(data, dict)):
        raise Exception(f'{data} is expected to be of dict type')

    if not data:
        return True

    for v in data.values():
        if isinstance(v, list):
            if len(v) > 0:
                return False
        else:
            if v is not None:
                return False

    return True


if __name__ == '__main__':
    def test_if_empty(data):
        print(f'{data} => {is_dict_empty(data)}')

    test_if_empty(None)
    test_if_empty({})
    test_if_empty({'a': None})
    test_if_empty({'a': None, 'b': None})
    test_if_empty({'a': None, 'b': None, 'c': []})
    test_if_empty({'a': []})
    test_if_empty({'a': [1]})
    test_if_empty({'a': [{}]})
    test_if_empty({'a': 0})
    test_if_empty({'a': ''})
