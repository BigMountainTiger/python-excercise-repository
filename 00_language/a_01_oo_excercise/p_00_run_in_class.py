class ExampleClass:

    print('Before defining __init__(self, value)')

    def __init__(self, value):
        self.value = value

    print('Before defining print_value(self)')

    def print_value(self):
        print(self.value)

    print('Done defining the methods')


if __name__ == '__main__':
    print()
    print('Create the objects')

    obj_1 = ExampleClass('value_1')
    obj_2 = ExampleClass('value_2')

    obj_1.print_value()
    obj_2.print_value()


print()
print('Conclusion')
print('In a class, the code out of the methods are only executed once, regardless how many instances is created')
