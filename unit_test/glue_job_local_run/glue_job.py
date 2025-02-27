import sys
from awsglue.utils import getResolvedOptions
import glue_job_dependency

# This is how glue get the parameters
# So it is important to take care of them in the test
print('Get the sys.argv')
print(sys.argv)

parameters = [
    'parameter_1',
    'parameter_2',
    'parameter_3'
]

print()
print('Parsed the parameters')
args = getResolvedOptions(sys.argv, parameters)
print(args['parameter_1'])
print(args['parameter_2'])
print(args['parameter_3'])

def A_function(v):
    print(v)

def print_dependency_value():
    glue_job_dependency.print_dependency_value()

if __name__ == '__main__':
    A_function('Callig the A_functon')