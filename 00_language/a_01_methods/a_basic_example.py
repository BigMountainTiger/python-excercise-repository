class example_class():
    def __init__(self, name):
        self.name = name

    def method_1(self):
        print(f'Print from {self.name}')


if __name__ == '__main__':

    o1 = example_class('instance 1')
    o2 = example_class('instance 2')

    print('The id of the instance method is different')
    print(id(o1.method_1))
    print(id(o2.method_1))

    print()
    print('Instance method remembers its context')
    m = o1.method_1
    m()
