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


if __name__ == "__main__":

    import example_package
    UserModules.print_user_modules()

    print('------------------------------')
    print(f'The name is absolute name:')
    print(f'  -> {example_package.example_module.__name__}\n')

    print(f'The file path is also absolute path:')
    print(f'  -> {example_package.example_module.__file__}\n')
