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
    import pkg_1

    # When importing a package, only the top-level init.py is loaded by default
    # If the __init__.py of the top-level does not import submodules, the submodule __init__.py files are not loaded automatically
    UserModules.print_user_modules()