# https://realpython.com/python-mutable-vs-immutable-types/#immutable-built-in-data-types-in-python

import unittest


class Test_class(unittest.TestCase):

    def test(self):
        d = {
            'key_1': 'value 1'
        }
        id1 = id(d)

        d['key_2'] = 'value 2'
        id2 = id(d)

        print(d)
        self.assertEqual(id1, id2)


if __name__ == '__main__':
    unittest.main()
