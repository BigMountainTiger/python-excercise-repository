class ParentClass:
    def parent_self(self):
        return self

class ChildClass(ParentClass):
     def child_self(self):
        return self

if __name__ == '__main__':
    
    obj = ChildClass()

    print(obj.__dict__)
    print(f'Parent self is the object -> {obj.parent_self() is obj}')
    print(f'Child self is the object -> {obj.child_self() is obj}')

    print()
    print(f'The same address => {hex(id(obj))} - {hex(id(obj.parent_self()))} - {hex(id(obj.child_self()))}')