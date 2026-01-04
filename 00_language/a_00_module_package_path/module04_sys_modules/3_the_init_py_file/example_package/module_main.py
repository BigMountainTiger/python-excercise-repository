from .module_sub import print_variable_in_submodule

def print_variable_in_submodule_wrapper():
    print("Calling print_variable_in_submodule from module_main:")
    print_variable_in_submodule()