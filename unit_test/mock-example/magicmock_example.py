import unittest
from unittest.mock import MagicMock


class TestMagicMock(unittest.TestCase):
    def test_magic_mock(self):
        mock = MagicMock()

        # 1. Mock property
        mock.first.second.text = 'Expected Text'
        self.assertEqual(mock.first.second.text, 'Expected Text')

        # 2. Mock function - return_value
        mock.first.mock_func.return_value = 'Expected return value'
        self.assertEqual(mock.first.mock_func(), 'Expected return value')

        # 3. side_effect
        mock.first.mock_func.side_effect = Exception('Mocked exception')
        self.assertRaises(Exception, mock.first.mock_func)

        # 4. side_effect can be an array
        mock.first.mock_func.side_effect = [
            'value 1', 'value 2', Exception('Mocked exception')]
        self.assertEqual(mock.first.mock_func(), 'value 1')
        self.assertEqual(mock.first.mock_func(), 'value 2')
        self.assertRaises(Exception, mock.first.mock_func)


if __name__ == '__main__':
    unittest.main()
