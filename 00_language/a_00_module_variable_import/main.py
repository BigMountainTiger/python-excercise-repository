from test_module import the_variable
import test_module


def run():
    test_module.increment()
    print(f'When access through the module - {test_module.the_variable}')
    print(f'When access directly - {the_variable}')

    print()
    print('Conclusion')
    print('1. A module is effectively imported as an object. Variables and functions in the module can be accessed by the reference to othe module')
    print('2. When "impor" a variable from a module, passing by value is effectively used. Any update to the variable in the module will not affect the imported variable')
    print('3. But the updated value in the module can be accessed through the reference of the module')
    print('')


if __name__ == '__main__':
    run()
