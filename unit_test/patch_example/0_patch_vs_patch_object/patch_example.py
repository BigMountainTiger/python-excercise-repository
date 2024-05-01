import unittest
from unittest.mock import patch
import A


class Test_patch(unittest.TestCase):

    @patch('B.b_text', return_value='New value')
    def test_mock(self, m):
        text = A.speak()

        print(f'The patch takes effect - {text}')
        self.assertEqual(text, 'New value')


if __name__ == '__main__':
    unittest.main()
