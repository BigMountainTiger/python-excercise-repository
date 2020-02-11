# A class with an instructor and an instance method
class AClass:
  def __init__(self, attr_1, attr_2):
    self.attr_1 = attr_1
    self.attr_2 = attr_2

  def print_attributes(self):
    print("{} - {}".format(self.attr_1, self.attr_2))

# Create two instances
obj_1 = AClass('obj_1_a1', 'obj_1_a2')
obj_2 = AClass('obj_2_a1', 'obj_2_a2')

# Call the instance method
# Each object has its own instance attributes
obj_1.print_attributes()
obj_2.print_attributes()
print()