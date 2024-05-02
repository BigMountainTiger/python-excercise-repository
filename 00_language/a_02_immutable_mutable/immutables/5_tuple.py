import unittest


class Test_class(unittest.TestCase):

    def test(self):
        t = ('a', 'b')
        id1 = id(t)

        t = ('a', 'b', 'c')
        id2 = id(t)

        print(f'{id1} - {id2}')
        self.assertNotEqual(id1, id2)


if __name__ == '__main__':
    unittest.main()
