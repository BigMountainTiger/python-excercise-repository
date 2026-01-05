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
    import pkg_1.pkg_2.pkg_3 as leaf_package

    # 1. Importing a leaf package similar to load leaf modules
    # it also forces loading of all parent packages' __init__.py files in the sub-tree in the order from top-level to the leaf package
    UserModules.print_user_modules()
