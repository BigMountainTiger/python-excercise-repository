def validate_sorted(d):
    item = d[0]
    for e in d:
        if item > e:
            raise Exception('List is not sorted')

        item = e
