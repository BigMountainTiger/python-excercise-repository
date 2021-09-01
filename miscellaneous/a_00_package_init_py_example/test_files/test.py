import sys

# Add the package path
sys.path
sys.path.append('../test_packages')

# With an empty init file is OK
from module_with_empty_init.sub_1 import module as m1
m1.printIt()

# __init__.py is no longer needed in higher version of python
# module_without_init folder does not have an __init__.py file
from module_without_init.sub_1 import module as m2
m2.printIt()


# Content can be added in __init__.py and can be imported directly
import module_with_init
module_with_init.PrintFromTop()

# No longer need to import "module_with_init.sub_1.module"
# It has been imported in the package "__init__.py" file
module_with_init.sub_1.module.printIt()

# module_1 is not imported in the package "__init__.py" file
# use it will have problem
try:
  module_with_init.sub_1.module_1.printIt()
except Exception as e:
  print(e)

# Need to import "module_1" directly
from module_with_init.sub_1 import module_1 as m3
m3.printIt()