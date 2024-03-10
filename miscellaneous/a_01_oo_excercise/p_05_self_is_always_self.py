GrandParentClass_object_ref = None
ParentClass_object_ref = None
ChildClass_object_ref = None


class GrandParentClass:
    def __init__(self):
        self.grand_parent_attr = 'Grand Parent Attribute'

        global GrandParentClass_object_ref
        GrandParentClass_object_ref = self

    def print(self):
        print("Print from grand parent class - {}".format(self.grand_parent_attr))


class ParentClass(GrandParentClass):
    def __init__(self):
        super().__init__()
        self.parent_attr = 'Parent Attribute'

        global ParentClass_object_ref
        ParentClass_object_ref = self

    def print(self):
        print("Print from parent class - {}".format(self.parent_attr))


class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        self.child_attr = 'Child Attribute'

        global ChildClass_object_ref
        ChildClass_object_ref = self

    def print(self):
        print("Print from child class - {}".format(self.child_attr))


if __name__ == '__main__':

    object = ChildClass()
    print('The self and the object always reference to the same memory address:')
    print(f'1. The object reference - {id(object)}')
    print(f'2. The self in child - {id(ChildClass_object_ref)}')
    print(f'3. The self in parent - {id(ParentClass_object_ref)}')
    print(f'4. The self in grand parent - {id(GrandParentClass_object_ref)}')
