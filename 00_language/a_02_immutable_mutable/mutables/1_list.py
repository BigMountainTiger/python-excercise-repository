# https://realpython.com/python-mutable-vs-immutable-types/#immutable-built-in-data-types-in-python

import unittest


class Test_class(unittest.TestCase):

    def test(self):
        l = [1, 2, 3]
        id1 = id(l)

        l.append(4)
        id2 = id(l)

        print(l)
        self.assertEqual(id1, id2)


if __name__ == '__main__':
    unittest.main()
