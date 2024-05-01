import unittest
import os
from unittest.mock import patch, Mock
import outter

# In the rest class directly import the monkies
from pkg_basic.inner import A, B
import pkg_basic


class TestMock(unittest.TestCase):

    def test_outter_00(self):
        MY_ENV = os.environ.get('MY_ENV')
        print(f'The MY_ENV is {MY_ENV}')

    def test_outter_01(self):
        EXPECTED = 'ABCD'
        self.assertEqual(outter.outter('ABCD'), EXPECTED)

    # Here we can patch multiple
    @patch.object(A, 'inner', Mock(return_value='This is OK'))
    @patch.object(B, 'echo', Mock(return_value='This is the mocked value'))
    def test_outter_02(self):
        self.assertEqual(outter.outter('ABCD'), 'This is OK')
        self.assertEqual(pkg_basic.inner.B().echo(
            'Anything'), 'This is the mocked value')

    def test_outter_03(self):
        EXPECTED = 'ABCD'
        self.assertEqual(outter.outter('ABCD'), EXPECTED)

    # patch.object can be used as a context manager
    def test_outter_04(self):
        with patch.object(A, 'inner') as mock_obj:
            mock_obj.return_value = 'OKKKKK'
            self.assertEqual(A().inner(''), 'OKKKKK')


if __name__ == '__main__':
    unittest.main()
