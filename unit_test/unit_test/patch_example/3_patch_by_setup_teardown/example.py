import unittest
from unittest.mock import patch
import A


class Test_patch(unittest.TestCase):

    def setUp(self):
        self.patcher = patch('A.func', return_value='New value')
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_mock(self):
        text = A.func()
        print(text)
        self.assertEqual(text, 'New value')


if __name__ == '__main__':
    unittest.main()
