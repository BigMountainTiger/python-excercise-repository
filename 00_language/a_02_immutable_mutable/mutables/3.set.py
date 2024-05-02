# https://realpython.com/python-mutable-vs-immutable-types/#immutable-built-in-data-types-in-python

import unittest


class Test_class(unittest.TestCase):

    def test(self):
        s = {'a', 'b', 'c'}
        id1 = id(s)

        # b wont be added multiple times
        s.add('b')
        s.add('d')
        id2 = id(s)

        print(s)
        self.assertEqual(id1, id2)


if __name__ == '__main__':
    unittest.main()
