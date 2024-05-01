import unittest
from unittest.mock import patch
import A


class Test_patch(unittest.TestCase):

    # No patch, so original function is called
    def test_original(self):
        text = A.func()
        self.assertEqual(text, 'The original value')

    # Note 'A.func' is the path that the func can be imported from this location
    @patch('A.func', return_value='New value')
    def test_mock(self, f):
        text = A.func()
        print(text)
        self.assertEqual(text, 'New value')


if __name__ == '__main__':
    unittest.main()
