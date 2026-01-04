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
    # Load the submodule
    from example_package import module_sub
    module_sub.variable_in_submodule = "Hello from run.py"

    UserModules.print_user_modules()

    # Load the main module which uses the submodule    
    from example_package.module_main import print_variable_in_submodule_wrapper
    print_variable_in_submodule_wrapper()

    UserModules.print_user_modules()

    # Conclusion: The same instance of module_sub is used in both imports
    # 1. The key of the sys.modules dictionary is the absolute module name (e.g., example_package.module_sub)
    # 2. When a relative import is used within a package, Python resolves it to the absolute module name
    # 3. It is safe to use relative imports within packages without worrying about creating multiple instances of the same module

    assert sys.modules['example_package.module_sub'] is module_sub