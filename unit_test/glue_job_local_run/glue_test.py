import os
import json
import unittest
from unittest.mock import patch

PARAMETERS = json.loads(os.environ['PARAMETERS'])
ARGV = ['glue_job.py']
for k, v in PARAMETERS.items():
    ARGV.append(k)
    ARGV.append(v)


class GlueTest(unittest.TestCase):
    @staticmethod
    def A_function(v):
        print(f'This is the patched function - {v}')

    @patch('glue_job.A_function', A_function)
    @patch('glue_job_dependency.dependency_value', 'Patched value here ...')
    @patch('sys.argv', ARGV)
    def test_run(self):
        # Need to import in the test function
        # because unittest seems not to allow sys.argv to have additional parameters
        import glue_job

        print('\nThe patched function is being called:')
        glue_job.A_function('OK')

        print('\nThe patched value is being printed')
        glue_job.print_dependency_value()


if __name__ == '__main__':
    unittest.main()
