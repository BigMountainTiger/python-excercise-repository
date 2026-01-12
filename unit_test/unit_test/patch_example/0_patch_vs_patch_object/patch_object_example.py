import unittest
from unittest.mock import patch, Mock
import A
import B


class Test_patch_object(unittest.TestCase):

    # patch.object patches an actual object
    @patch.object(B, 'b_text', Mock(return_value='New value'))
    def test_mock(self):
        text = A.speak()

        print(f'The patch takes effect - {text}')
        self.assertEqual(text, 'New value')


if __name__ == '__main__':
    unittest.main()
