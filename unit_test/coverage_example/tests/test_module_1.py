
import unittest
from src import module_1


class TestModule_1(unittest.TestCase):

    def test_module_1(self):
        module_1.func(0)
        module_1.func(1)
        module_1.func(2)
        module_1.func(3)
