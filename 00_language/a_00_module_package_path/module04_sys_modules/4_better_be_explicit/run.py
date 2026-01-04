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
    
    import the_module
    import example_package

    print("The top-level who_am_i() will be called even though example_package also has the_module.py")
    example_package.the_module.who_am_i()

    UserModules.print_user_modules()

    # actually, the the_module.py from example_package is not loaded
    assert 'example_package.the_module' not in sys.modules.keys()