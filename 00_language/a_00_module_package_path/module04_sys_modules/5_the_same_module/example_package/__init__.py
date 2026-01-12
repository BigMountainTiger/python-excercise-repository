# Use relative imports to include submodules in the package
# Python resolves these relative imports to absolute module names
from . import module_main
from . import module_sub

print('__init__.py is called')