# https://realpython.com/python-mutable-vs-immutable-types/#immutable-built-in-data-types-in-python

# https://www.w3schools.com/python/ref_func_id.asp
# The id() function returns a unique id for the specified object.

import unittest


class Test_class(unittest.TestCase):

    def test(self):
        number = 314
        id1 = id(number)

        # re-assign change the id
        number += 1
        id2 = id(number)

        print(f'{id1} - {id2}')
        self.assertNotEqual(id1, id2)


if __name__ == '__main__':
    unittest.main()
