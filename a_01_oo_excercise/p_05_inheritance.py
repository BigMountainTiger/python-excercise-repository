# The parent class
class ParentClass:
  def __init__(self):
    self.parent_attr = 'Parent Attribute'

  def print(self):
    print("Print from parent class - {}".format(self.parent_attr))

# The child class
class ChildClass(ParentClass):
  def __init__(self):
    super().__init__()
    self.child_attr = 'Child Attribute'

  def print(self):
    print("Print from child class - {}".format(self.child_attr))
  
# Create instances for both classes
# and call the print method
parent_obj = ParentClass()
parent_obj.print()

child_obj = ChildClass()
child_obj.print()
print()

# The the polymophism behavior, kind of ...
print('Test polymophism')
objects = [parent_obj, child_obj]
for obj in objects:
  obj.print()