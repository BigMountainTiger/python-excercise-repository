import unittest


class Test_class(unittest.TestCase):

    def test(self):
        # boolean is a subclass of int
        print(f'boolean is a subclass of int - {issubclass(bool, int)}')

        b = True
        id1 = id(b)

        b = False
        id2 = id(b)

        print(f'{id1} - {id2}')
        self.assertNotEqual(id1, id2)


if __name__ == '__main__':
    unittest.main()
