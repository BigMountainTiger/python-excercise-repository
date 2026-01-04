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
        for k, v in cls.user_modules().items():
            print(k)
            print(f'  -> {v.__file__}\n')

if __name__ == '__main__':
    # It is not a run-time error to import a package without __init__.py
    # But it is just a namespace and no module is loaded until you import the modules directly
    import package_1

    # A package without __init__.py the __file__ attribute is None, it is just a namespace package
    # Need to import the module in it explicitly to use the module
    assert package_1.__file__ is None

    UserModules.print_user_modules()