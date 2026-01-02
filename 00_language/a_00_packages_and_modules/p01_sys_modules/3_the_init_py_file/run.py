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
    
    import example_package

    # With the __init__.py file, when we import the package, both submodules are loaded
    UserModules.print_user_modules()

    print()
    example_package.module_sub.variable_in_submodule = "Hello from run.py"
    example_package.module_main.print_variable_in_submodule_wrapper()
