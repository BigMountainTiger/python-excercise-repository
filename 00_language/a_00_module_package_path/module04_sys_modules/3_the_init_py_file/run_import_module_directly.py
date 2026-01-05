import sys


class UserModules:
    # A simple utility to print user-defined modules loaded in sys.modules
    _system_modules = set(sys.modules.keys())

    @classmethod
    def user_modules(cls):
        return {k: v for k, v in sys.modules.items() if k not in cls._system_modules}

    @classmethod
    def print_user_modules(cls):
        print()
        for k, _ in cls.user_modules().items():
            print(k)


if __name__ == "__main__":
    
    import example_package.module_sub as module_sub

    # Even only importing the submodule directly, the __init__.py file of the package is executed
    UserModules.print_user_modules()

    print()
    module_sub.variable_in_submodule = "Hello from run.py"
    module_sub.print_variable_in_submodule()
