import unittest
from unittest.mock import MagicMock


class TestMagicMock(unittest.TestCase):
    def test_magic_mock(self):
        mock = MagicMock()

        mock.a.b.c = 'Expected Text'
        mock.a.call_with_return_Value.return_value = 'Expected return value'
        mock.a.call_with_side_effect_exception.side_effect = Exception(
            'Mocked exception')
        mock.a.call_with_side_effect_array.side_effect = ['Value 1', 'Value 2']

        def actual_function(param_1):
            return param_1

        mock.a.b.actual_function = actual_function

        # 1. attribute, multiple layer is OK
        self.assertEqual('Expected Text', mock.a.b.c)

        # 2. function return value
        self.assertEqual('Expected return value',
                         mock.a.call_with_return_Value())

        # 3. side_effect exception, exception is thrown at every invocation
        for i in range(0, 2):
            try:
                mock.a.call_with_side_effect_exception()
            except Exception as e:
                self.assertEqual('Mocked exception', str(e))

        # 4. side_effect array, different value at different invocation
        self.assertEqual('Value 1',
                         mock.a.call_with_side_effect_array())
        self.assertEqual('Value 2',
                         mock.a.call_with_side_effect_array())

        with self.assertRaises(Exception):
            mock.a.call_with_side_effect_array()

        # 5. call an actual function
        self.assertEqual(
            'A Parameter', mock.a.b.actual_function('A Parameter'))

        mock.a.wwww()


if __name__ == '__main__':
    unittest.main()
