# When there is a module named the_module.py already loaded in sys.modules,
# the the_module.py inside example_package will not be loaded

# to avoid confusion, we should be explicit about which module to use
# either by relative (using . or .. or ..., etc.) or absolute imports

# This import will cause confusion, it will import the top-level the_module.py
# if we intend to import the the_module.py inside the example_package.
import the_module

# the correct way is:
# from . import the_module or from example_package import the_module
