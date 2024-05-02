import unittest


class Test_class(unittest.TestCase):

    def test(self):
        b = b'text'
        id1 = id(b)

        b = b'text - 1'
        id2 = id(b)

        print(f'{id1} - {id2}')
        self.assertNotEqual(id1, id2)


if __name__ == '__main__':
    unittest.main()
