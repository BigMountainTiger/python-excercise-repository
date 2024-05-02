import unittest


class Test_class(unittest.TestCase):

    def test(self):
        s = 'text'
        id1 = id(s)

        s = 'text - 1'
        id2 = id(s)

        print(f'{id1} - {id2}')
        self.assertNotEqual(id1, id2)


if __name__ == '__main__':
    unittest.main()
